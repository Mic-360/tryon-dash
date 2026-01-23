"""Logs page with Catppuccin Mocha theme."""

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


def filter_input(label: str, placeholder: str, value: rx.Var, on_change, icon: str = None) -> rx.Component:
    """Create a labeled filter input field with Catppuccin styling."""
    return rx.vstack(
        rx.hstack(
            rx.cond(
                icon is not None,
                rx.icon(icon, size=12, style={"color": COLORS["overlay1"]}),
                rx.fragment(),
            ) if icon else rx.fragment(),
            rx.text(
                label,
                style={"color": COLORS["subtext0"]},
                class_name="text-xs font-medium uppercase tracking-wide",
            ),
            class_name="gap-1.5 items-center",
        ),
        rx.input(
            placeholder=placeholder,
            value=value,
            on_change=on_change,
            style={
                "background": COLORS["surface0"],
                "borderColor": COLORS["surface1"],
                "color": COLORS["text"],
            },
            class_name="rounded-lg border px-3 py-2.5 text-sm w-full focus:border-[#b4befe] focus:ring-1 focus:ring-[#b4befe] placeholder:text-[#6c7086] transition-colors",
        ),
        class_name="gap-1.5 w-full",
    )


def log_card(log: dict) -> rx.Component:
    """Render a single log entry card with Catppuccin styling."""
    return rx.box(
        # Header
        rx.hstack(
            rx.hstack(
                rx.box(
                    rx.text(
                        "#",
                        style={"color": COLORS["overlay0"]},
                        class_name="text-xs",
                    ),
                    rx.text(
                        log["_id"],
                        style={"color": COLORS["text"]},
                        class_name="font-mono text-xs truncate max-w-24",
                    ),
                    style={"background": COLORS["surface0"]},
                    class_name="flex items-center gap-1 px-2.5 py-1 rounded-md",
                ),
                rx.box(
                    rx.text(
                        log["clothType"],
                        style={"color": COLORS["green"]},
                        class_name="text-xs font-medium",
                    ),
                    style={"background": f"{COLORS['green']}20"},
                    class_name="px-2.5 py-1 rounded-full",
                ),
                class_name="gap-3 items-center",
            ),
            rx.hstack(
                rx.icon("calendar", size=14, style={"color": COLORS["overlay0"]}),
                rx.moment(
                    log["created_at"],
                    format="MMM DD, YYYY HH:mm",
                    style={"color": COLORS["subtext0"]},
                    class_name="text-sm",
                ),
                class_name="gap-2 items-center",
            ),
            style={"borderColor": COLORS["surface0"]},
            class_name="justify-between items-center pb-4 border-b flex-wrap gap-2",
        ),
        # Content Grid
        rx.box(
            # IDs Column
            rx.vstack(
                rx.hstack(
                    rx.box(
                        rx.icon("user", size=14, style={"color": COLORS["blue"]}),
                        style={"background": f"{COLORS['blue']}20"},
                        class_name="w-8 h-8 rounded-lg flex items-center justify-center",
                    ),
                    rx.vstack(
                        rx.text(
                            "User ID",
                            style={"color": COLORS["overlay0"]},
                            class_name="text-xs",
                        ),
                        rx.text(
                            log["userId"],
                            style={"color": COLORS["text"]},
                            class_name="text-sm font-medium truncate max-w-36",
                        ),
                        class_name="gap-0.5 items-start",
                    ),
                    class_name="gap-3 items-center",
                ),
                rx.hstack(
                    rx.box(
                        rx.icon("building", size=14, style={"color": COLORS["mauve"]}),
                        style={"background": f"{COLORS['mauve']}20"},
                        class_name="w-8 h-8 rounded-lg flex items-center justify-center",
                    ),
                    rx.vstack(
                        rx.text(
                            "Business ID",
                            style={"color": COLORS["overlay0"]},
                            class_name="text-xs",
                        ),
                        rx.text(
                            log["businessId"],
                            style={"color": COLORS["text"]},
                            class_name="text-sm font-medium truncate max-w-36",
                        ),
                        class_name="gap-0.5 items-start",
                    ),
                    class_name="gap-3 items-center",
                ),
                rx.hstack(
                    rx.box(
                        rx.icon("package", size=14, style={"color": COLORS["teal"]}),
                        style={"background": f"{COLORS['teal']}20"},
                        class_name="w-8 h-8 rounded-lg flex items-center justify-center",
                    ),
                    rx.vstack(
                        rx.text(
                            "Product ID",
                            style={"color": COLORS["overlay0"]},
                            class_name="text-xs",
                        ),
                        rx.text(
                            log["productId"],
                            style={"color": COLORS["text"]},
                            class_name="text-sm font-medium truncate max-w-36",
                        ),
                        class_name="gap-0.5 items-start",
                    ),
                    class_name="gap-3 items-center",
                ),
                class_name="gap-4",
            ),
            # Technical Details Column
            rx.vstack(
                rx.hstack(
                    rx.box(
                        rx.icon("hash", size=14, style={"color": COLORS["peach"]}),
                        style={"background": f"{COLORS['peach']}20"},
                        class_name="w-8 h-8 rounded-lg flex items-center justify-center",
                    ),
                    rx.vstack(
                        rx.text(
                            "Inference Steps",
                            style={"color": COLORS["overlay0"]},
                            class_name="text-xs",
                        ),
                        rx.text(
                            log["num_inference_steps"],
                            style={"color": COLORS["text"]},
                            class_name="text-sm font-medium",
                        ),
                        class_name="gap-0.5 items-start",
                    ),
                    class_name="gap-3 items-center",
                ),
                rx.hstack(
                    rx.box(
                        rx.icon("zap", size=14, style={"color": COLORS["yellow"]}),
                        style={"background": f"{COLORS['yellow']}20"},
                        class_name="w-8 h-8 rounded-lg flex items-center justify-center",
                    ),
                    rx.vstack(
                        rx.text(
                            "Seed",
                            style={"color": COLORS["overlay0"]},
                            class_name="text-xs",
                        ),
                        rx.text(
                            log["seed"],
                            style={"color": COLORS["text"]},
                            class_name="text-sm font-medium",
                        ),
                        class_name="gap-0.5 items-start",
                    ),
                    class_name="gap-3 items-center",
                ),
                rx.hstack(
                    rx.box(
                        rx.icon("sliders-horizontal", size=14, style={"color": COLORS["pink"]}),
                        style={"background": f"{COLORS['pink']}20"},
                        class_name="w-8 h-8 rounded-lg flex items-center justify-center",
                    ),
                    rx.vstack(
                        rx.text(
                            "Guidance Scale",
                            style={"color": COLORS["overlay0"]},
                            class_name="text-xs",
                        ),
                        rx.text(
                            log["guidance_scale"],
                            style={"color": COLORS["text"]},
                            class_name="text-sm font-medium",
                        ),
                        class_name="gap-0.5 items-start",
                    ),
                    class_name="gap-3 items-center",
                ),
                class_name="gap-4",
            ),
            # Images Column
            rx.hstack(
                rx.vstack(
                    rx.text(
                        "Person",
                        style={"color": COLORS["overlay0"]},
                        class_name="text-xs font-medium",
                    ),
                    rx.image(
                        src="https://devbackendpersonimage.s3.ap-south-1.amazonaws.com/" + log["personImage"].to(str),
                        style={"borderColor": COLORS["surface1"]},
                        class_name="w-20 h-20 object-cover rounded-lg border",
                    ),
                    class_name="gap-1.5 items-center",
                ),
                rx.vstack(
                    rx.text(
                        "Cloth",
                        style={"color": COLORS["overlay0"]},
                        class_name="text-xs font-medium",
                    ),
                    rx.image(
                        src="https://devbackendclothimage.s3.ap-south-1.amazonaws.com/" + log["clothImage"].to(str),
                        style={"borderColor": COLORS["surface1"]},
                        class_name="w-20 h-20 object-cover rounded-lg border",
                    ),
                    class_name="gap-1.5 items-center",
                ),
                rx.vstack(
                    rx.text(
                        "Result",
                        style={"color": COLORS["overlay0"]},
                        class_name="text-xs font-medium",
                    ),
                    rx.image(
                        src="https://devbackendresultimage.s3.ap-south-1.amazonaws.com/" + log["resultImage"].to(str),
                        style={"borderColor": COLORS["surface1"]},
                        class_name="w-20 h-20 object-cover rounded-lg border",
                    ),
                    class_name="gap-1.5 items-center",
                ),
                class_name="gap-4",
            ),
            class_name="grid grid-cols-1 md:grid-cols-3 gap-6 py-5",
        ),
        # Footer
        rx.hstack(
            rx.hstack(
                rx.box(
                    rx.icon("circle-check", size=12, style={"color": COLORS["green"]}),
                    style={"background": f"{COLORS['green']}20"},
                    class_name="w-6 h-6 rounded-full flex items-center justify-center",
                ),
                rx.text(
                    "Processing Complete",
                    style={"color": COLORS["subtext0"]},
                    class_name="text-sm",
                ),
                class_name="gap-2 items-center",
            ),
            style={"borderColor": COLORS["surface0"]},
            class_name="pt-4 border-t",
        ),
        style={"background": COLORS["mantle"], "borderColor": COLORS["surface0"]},
        class_name="rounded-xl border p-5 hover:border-[#45475a] transition-colors duration-200",
    )


def logs_page() -> rx.Component:
    """Logs page content with Catppuccin Mocha theme."""
    return layout(
        rx.box(
            # Header
            rx.hstack(
                rx.vstack(
                    rx.text(
                        "Logs Dashboard",
                        style={"color": COLORS["text"]},
                        class_name="text-2xl font-bold",
                    ),
                    rx.text(
                        "Real-time processing logs and analytics",
                        style={"color": COLORS["subtext0"]},
                    ),
                    class_name="gap-1 items-start",
                ),
                rx.button(
                    rx.icon("refresh-cw", size=16),
                    "Refresh",
                    on_click=AppState.fetch_logs,
                    style={"background": COLORS["mauve"], "color": COLORS["crust"]},
                    class_name="font-medium px-4 py-2 rounded-lg gap-2 hover:opacity-90 transition-opacity cursor-pointer",
                    loading=AppState.logs_loading,
                ),
                class_name="justify-between items-center mb-6 flex-wrap gap-4",
            ),
            # Filters
            rx.box(
                rx.hstack(
                    rx.hstack(
                        rx.box(
                            rx.icon("filter", size=16, style={"color": COLORS["mauve"]}),
                            style={"background": f"{COLORS['mauve']}20"},
                            class_name="w-8 h-8 rounded-lg flex items-center justify-center",
                        ),
                        rx.vstack(
                            rx.text(
                                "Filters",
                                style={"color": COLORS["text"]},
                                class_name="text-lg font-semibold",
                            ),
                            rx.text(
                                "Narrow down your results",
                                style={"color": COLORS["subtext0"]},
                                class_name="text-xs",
                            ),
                            class_name="gap-0 items-start",
                        ),
                        class_name="gap-3 items-center",
                    ),
                    rx.button(
                        rx.icon("x", size=14),
                        "Clear All",
                        on_click=[
                            AppState.set_filter_user_id(""),
                            AppState.set_filter_business_id(""),
                            AppState.set_filter_product_id(""),
                            AppState.set_filter_cloth_type("__all__"),
                            AppState.set_filter_inference_steps(""),
                            AppState.set_filter_seed(""),
                            AppState.set_filter_guidance_scale(""),
                            AppState.set_filter_date(""),
                        ],
                        style={"background": COLORS["surface0"], "color": COLORS["subtext1"]},
                        class_name="text-xs font-medium px-3 py-1.5 rounded-lg gap-1.5 hover:bg-[#45475a] cursor-pointer transition-colors",
                    ),
                    class_name="justify-between items-center mb-5",
                ),
                # Filter Groups
                rx.vstack(
                    # Row 1: ID Filters
                    rx.box(
                        filter_input("User ID", "Search by user ID...", AppState.filter_user_id, AppState.set_filter_user_id),
                        filter_input("Business ID", "Search by business ID...", AppState.filter_business_id, AppState.set_filter_business_id),
                        filter_input("Product ID", "Search by product ID...", AppState.filter_product_id, AppState.set_filter_product_id),
                        rx.vstack(
                            rx.text(
                                "Cloth Type",
                                style={"color": COLORS["subtext0"]},
                                class_name="text-xs font-medium uppercase tracking-wide",
                            ),
                            rx.select.root(
                                rx.select.trigger(
                                    placeholder="All Types",
                                    style={
                                        "background": COLORS["surface0"],
                                        "borderColor": COLORS["surface1"],
                                        "color": COLORS["text"],
                                    },
                                    class_name="rounded-lg border w-full h-[42px]",
                                ),
                                rx.select.content(
                                    rx.select.item("All Types", value="__all__"),
                                    rx.foreach(
                                        AppState.unique_cloth_types,
                                        lambda t: rx.select.item(t, value=t),
                                    ),
                                    style={"background": COLORS["surface0"]},
                                ),
                                value=rx.cond(
                                    AppState.filter_cloth_type == "",
                                    "__all__",
                                    AppState.filter_cloth_type,
                                ),
                                on_change=AppState.set_filter_cloth_type,
                            ),
                            class_name="gap-1.5 w-full",
                        ),
                        class_name="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4",
                    ),
                    # Row 2: Technical Filters
                    rx.box(
                        filter_input("Inference Steps", "e.g. 30", AppState.filter_inference_steps, AppState.set_filter_inference_steps),
                        filter_input("Seed", "e.g. 42", AppState.filter_seed, AppState.set_filter_seed),
                        filter_input("Guidance Scale", "e.g. 7.5", AppState.filter_guidance_scale, AppState.set_filter_guidance_scale),
                        rx.vstack(
                            rx.text(
                                "Date",
                                style={"color": COLORS["subtext0"]},
                                class_name="text-xs font-medium uppercase tracking-wide",
                            ),
                            rx.input(
                                type="date",
                                value=AppState.filter_date,
                                on_change=AppState.set_filter_date,
                                style={
                                    "background": COLORS["surface0"],
                                    "borderColor": COLORS["surface1"],
                                    "color": COLORS["text"],
                                },
                                class_name="rounded-lg border px-3 py-2.5 text-sm w-full transition-colors",
                            ),
                            class_name="gap-1.5 w-full",
                        ),
                        class_name="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4",
                    ),
                    class_name="gap-4",
                ),
                style={"background": COLORS["mantle"], "borderColor": COLORS["surface0"]},
                class_name="rounded-xl border p-5 mb-6",
            ),
            # Loading State
            rx.cond(
                AppState.logs_loading,
                rx.center(
                    rx.vstack(
                        rx.spinner(size="3"),
                        rx.text(
                            "Loading logs...",
                            style={"color": COLORS["subtext0"]},
                        ),
                        class_name="gap-3 items-center py-12",
                    ),
                ),
                rx.fragment(),
            ),
            # Logs List
            rx.cond(
                ~AppState.logs_loading,
                rx.cond(
                    AppState.filtered_logs.length() > 0,
                    rx.vstack(
                        rx.foreach(AppState.filtered_logs, log_card),
                        class_name="gap-4",
                    ),
                    rx.center(
                        rx.vstack(
                            rx.box(
                                rx.icon("inbox", size=32, style={"color": COLORS["overlay0"]}),
                                style={"background": COLORS["surface0"]},
                                class_name="w-16 h-16 rounded-full flex items-center justify-center",
                            ),
                            rx.text(
                                "No logs available",
                                style={"color": COLORS["text"]},
                                class_name="text-lg font-medium",
                            ),
                            rx.text(
                                "Try adjusting your filters or click refresh to check for new logs.",
                                style={"color": COLORS["subtext0"]},
                                class_name="text-sm text-center",
                            ),
                            style={"background": COLORS["mantle"], "borderColor": COLORS["surface0"]},
                            class_name="gap-3 items-center py-12 rounded-xl border w-full",
                        ),
                    ),
                ),
                rx.fragment(),
            ),
            class_name="p-6 md:p-8 max-w-7xl mx-auto",
            on_mount=AppState.fetch_logs,
        ),
    )
