"""Dashboard/Home page with Catppuccin Mocha theme."""

import reflex as rx
from ..state import AppState
from ..components.layout import layout


# Catppuccin Mocha color palette
COLORS = {
    "base": "#1e1e2e",
    "mantle": "#181825",
    "crust": "#11111b",
    "surface0": "#313244",
    "surface1": "#45475a",
    "surface2": "#585b70",
    "overlay0": "#6c7086",
    "overlay1": "#7f849c",
    "text": "#cdd6f4",
    "subtext0": "#a6adc8",
    "subtext1": "#bac2de",
    "lavender": "#b4befe",
    "blue": "#89b4fa",
    "sapphire": "#74c7ec",
    "teal": "#94e2d5",
    "green": "#a6e3a1",
    "yellow": "#f9e2af",
    "peach": "#fab387",
    "mauve": "#cba6f7",
    "pink": "#f5c2e7",
    "red": "#f38ba8",
}


def stat_card(title: str, value, icon: str, color: str) -> rx.Component:
    """Create a statistics card with Catppuccin styling."""
    icon_color = COLORS.get(color, COLORS["mauve"])
    
    return rx.box(
        rx.hstack(
            rx.box(
                rx.icon(icon, size=22, style={"color": icon_color}),
                style={"background": f"{icon_color}20"},
                class_name="w-12 h-12 rounded-xl flex items-center justify-center",
            ),
            rx.vstack(
                rx.text(
                    title,
                    style={"color": COLORS["subtext0"]},
                    class_name="text-sm font-medium",
                ),
                rx.text(
                    value,
                    style={"color": COLORS["text"]},
                    class_name="text-2xl font-bold",
                ),
                class_name="gap-0.5 items-start",
            ),
            class_name="gap-4 items-center",
        ),
        style={"background": COLORS["mantle"], "borderColor": COLORS["surface0"]},
        class_name="rounded-xl p-5 border hover:border-[#45475a] transition-colors duration-200",
    )


def business_row(business: dict) -> rx.Component:
    """Render a single business table row."""
    return rx.table.row(
        rx.table.cell(
            rx.hstack(
                rx.box(
                    rx.icon("building-2", size=18, style={"color": COLORS["mauve"]}),
                    style={"background": COLORS["surface0"]},
                    class_name="w-10 h-10 rounded-full flex items-center justify-center",
                ),
                rx.vstack(
                    rx.text(
                        business["businessName"],
                        style={"color": COLORS["text"]},
                        class_name="font-semibold",
                    ),
                    rx.text(
                        business["businessEmail"],
                        style={"color": COLORS["subtext0"]},
                        class_name="text-sm",
                    ),
                    class_name="gap-0.5 items-start",
                ),
                class_name="gap-3 items-center",
            ),
        ),
        rx.table.cell(
            rx.moment(
                business["businessCreated_at"],
                format="MMM DD, YYYY",
            ),
            style={"color": COLORS["subtext1"]},
        ),
        rx.table.cell(
            rx.hstack(
                rx.cond(
                    AppState.visible_keys.contains(business["_id"]),
                    rx.code(
                        business["businessAPIKey"],
                        style={"background": COLORS["surface0"], "color": COLORS["green"]},
                        class_name="text-xs px-2 py-1 rounded",
                    ),
                    rx.text(
                        "••••••••••••",
                        style={"color": COLORS["overlay0"]},
                        class_name="font-mono",
                    ),
                ),
                rx.button(
                    rx.cond(
                        AppState.visible_keys.contains(business["_id"]),
                        rx.icon("eye-off", size=16, style={"color": COLORS["overlay1"]}),
                        rx.icon("eye", size=16, style={"color": COLORS["overlay1"]}),
                    ),
                    on_click=AppState.toggle_key_visibility(business["_id"]),
                    variant="ghost",
                    size="1",
                    class_name="hover:bg-[#313244] cursor-pointer rounded-lg p-1.5",
                ),
                class_name="gap-2 items-center",
            ),
        ),
        rx.table.cell(
            rx.box(
                rx.text(
                    "Active",
                    style={"color": COLORS["green"]},
                    class_name="text-xs font-medium",
                ),
                style={"background": f"{COLORS['green']}20"},
                class_name="px-2.5 py-1 rounded-full inline-block",
            ),
        ),
        class_name="hover:bg-[#313244]/30 transition-colors",
    )


def add_business_modal() -> rx.Component:
    """Add business modal dialog with Catppuccin styling."""
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(
                rx.icon("plus", size=18),
                "Add Business",
                style={"background": COLORS["mauve"], "color": COLORS["crust"]},
                class_name="font-medium px-4 py-2 rounded-lg gap-2 hover:opacity-90 transition-opacity cursor-pointer",
            ),
        ),
        rx.dialog.content(
            rx.dialog.title(
                "Add New Business",
                style={"color": COLORS["text"]},
                class_name="text-xl font-bold",
            ),
            rx.dialog.description(
                "Fill in the details to create a new business account.",
                style={"color": COLORS["subtext0"]},
                class_name="mb-6",
            ),
            rx.vstack(
                rx.cond(
                    AppState.error != "",
                    rx.box(
                        rx.hstack(
                            rx.icon("circle-alert", size=16, style={"color": COLORS["red"]}),
                            rx.text(AppState.error, style={"color": COLORS["red"]}),
                            class_name="gap-2 items-center",
                        ),
                        style={"background": f"{COLORS['red']}20", "borderColor": f"{COLORS['red']}40"},
                        class_name="p-3 rounded-lg border mb-4",
                    ),
                    rx.fragment(),
                ),
                rx.vstack(
                    rx.text(
                        "Business Name",
                        style={"color": COLORS["subtext1"]},
                        class_name="text-sm font-medium",
                    ),
                    rx.input(
                        placeholder="Enter business name",
                        value=AppState.form_name,
                        on_change=AppState.set_form_name,
                        style={
                            "background": COLORS["surface0"],
                            "borderColor": COLORS["surface1"],
                            "color": COLORS["text"],
                        },
                        class_name="w-full rounded-lg border focus:border-[#b4befe] focus:ring-1 focus:ring-[#b4befe]",
                    ),
                    class_name="gap-1.5 w-full",
                ),
                rx.vstack(
                    rx.text(
                        "Email",
                        style={"color": COLORS["subtext1"]},
                        class_name="text-sm font-medium",
                    ),
                    rx.input(
                        placeholder="Enter email address",
                        type="email",
                        value=AppState.form_email,
                        on_change=AppState.set_form_email,
                        style={
                            "background": COLORS["surface0"],
                            "borderColor": COLORS["surface1"],
                            "color": COLORS["text"],
                        },
                        class_name="w-full rounded-lg border focus:border-[#b4befe] focus:ring-1 focus:ring-[#b4befe]",
                    ),
                    class_name="gap-1.5 w-full",
                ),
                rx.vstack(
                    rx.text(
                        "Password",
                        style={"color": COLORS["subtext1"]},
                        class_name="text-sm font-medium",
                    ),
                    rx.input(
                        placeholder="Enter password",
                        type="password",
                        value=AppState.form_password,
                        on_change=AppState.set_form_password,
                        style={
                            "background": COLORS["surface0"],
                            "borderColor": COLORS["surface1"],
                            "color": COLORS["text"],
                        },
                        class_name="w-full rounded-lg border focus:border-[#b4befe] focus:ring-1 focus:ring-[#b4befe]",
                    ),
                    class_name="gap-1.5 w-full",
                ),
                class_name="gap-4 w-full",
            ),
            rx.hstack(
                rx.dialog.close(
                    rx.button(
                        "Cancel",
                        style={"background": COLORS["surface0"], "color": COLORS["text"]},
                        class_name="px-4 py-2 rounded-lg hover:bg-[#45475a] cursor-pointer",
                    ),
                ),
                rx.button(
                    rx.cond(
                        AppState.is_submitting,
                        rx.hstack(
                            rx.spinner(size="1"),
                            rx.text("Creating..."),
                            class_name="gap-2",
                        ),
                        rx.text("Create Business"),
                    ),
                    on_click=AppState.create_business,
                    disabled=AppState.is_submitting,
                    style={"background": COLORS["mauve"], "color": COLORS["crust"]},
                    class_name="px-4 py-2 rounded-lg hover:opacity-90 cursor-pointer font-medium",
                ),
                class_name="gap-3 justify-end mt-6",
            ),
            style={"background": COLORS["mantle"], "borderColor": COLORS["surface0"]},
            class_name="max-w-md border",
        ),
    )


def dashboard_page() -> rx.Component:
    """Dashboard page content with Catppuccin Mocha theme."""
    return layout(
        rx.box(
            # Header
            rx.hstack(
                rx.vstack(
                    rx.text(
                        "Dashboard",
                        style={"color": COLORS["text"]},
                        class_name="text-2xl font-bold",
                    ),
                    rx.text(
                        "Manage your businesses and API keys",
                        style={"color": COLORS["subtext0"]},
                    ),
                    class_name="gap-1 items-start",
                ),
                add_business_modal(),
                class_name="justify-between items-center mb-8 flex-wrap gap-4",
            ),
            # Stats Grid
            rx.box(
                stat_card("Total Businesses", AppState.businesses.length(), "building-2", "mauve"),
                stat_card("Active Today", "12", "activity", "green"),
                stat_card("API Calls", "1,234", "zap", "yellow"),
                stat_card("Success Rate", "99.8%", "circle-check", "teal"),
                class_name="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 mb-8",
            ),
            # Businesses Table
            rx.box(
                rx.hstack(
                    rx.vstack(
                        rx.text(
                            "Businesses",
                            style={"color": COLORS["text"]},
                            class_name="text-lg font-semibold",
                        ),
                        rx.text(
                            "A list of all registered businesses",
                            style={"color": COLORS["subtext0"]},
                            class_name="text-sm",
                        ),
                        class_name="gap-0.5 items-start",
                    ),
                    rx.button(
                        rx.icon("refresh-cw", size=16),
                        "Refresh",
                        on_click=AppState.fetch_businesses,
                        style={"background": COLORS["surface0"], "color": COLORS["text"]},
                        class_name="gap-2 px-3 py-2 rounded-lg hover:bg-[#45475a] cursor-pointer",
                        loading=AppState.is_loading,
                    ),
                    class_name="justify-between items-center mb-4",
                ),
                rx.cond(
                    AppState.is_loading,
                    rx.center(
                        rx.spinner(size="3"),
                        class_name="py-12",
                    ),
                    rx.cond(
                        AppState.businesses.length() > 0,
                        rx.table.root(
                            rx.table.header(
                                rx.table.row(
                                    rx.table.column_header_cell(
                                        "Business",
                                        style={"color": COLORS["subtext0"]},
                                        class_name="font-medium",
                                    ),
                                    rx.table.column_header_cell(
                                        "Created",
                                        style={"color": COLORS["subtext0"]},
                                        class_name="font-medium",
                                    ),
                                    rx.table.column_header_cell(
                                        "API Key",
                                        style={"color": COLORS["subtext0"]},
                                        class_name="font-medium",
                                    ),
                                    rx.table.column_header_cell(
                                        "Status",
                                        style={"color": COLORS["subtext0"]},
                                        class_name="font-medium",
                                    ),
                                ),
                            ),
                            rx.table.body(
                                rx.foreach(AppState.businesses, business_row),
                            ),
                            class_name="w-full",
                        ),
                        rx.center(
                            rx.vstack(
                                rx.box(
                                    rx.icon("inbox", size=32, style={"color": COLORS["overlay0"]}),
                                    style={"background": COLORS["surface0"]},
                                    class_name="w-16 h-16 rounded-full flex items-center justify-center",
                                ),
                                rx.text(
                                    "No businesses yet",
                                    style={"color": COLORS["text"]},
                                    class_name="font-medium",
                                ),
                                rx.text(
                                    "Click 'Add Business' to create your first one.",
                                    style={"color": COLORS["subtext0"]},
                                    class_name="text-sm",
                                ),
                                class_name="gap-3 items-center py-12",
                            ),
                        ),
                    ),
                ),
                style={"background": COLORS["mantle"], "borderColor": COLORS["surface0"]},
                class_name="rounded-xl border p-6",
            ),
            class_name="p-6 md:p-8 max-w-7xl mx-auto",
            on_mount=AppState.fetch_businesses,
        ),
    )
