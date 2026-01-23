"""Sidebar component for navigation with Catppuccin Mocha theme."""

import reflex as rx
from ..state import AppState


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


def sidebar_link(text: str, href: str, icon: str) -> rx.Component:
    """Create a sidebar navigation link."""
    return rx.link(
        rx.hstack(
            rx.icon(
                icon, 
                size=20, 
                style={"color": COLORS["overlay1"]},
                class_name="group-hover:text-[#b4befe] transition-colors duration-200",
            ),
            rx.cond(
                ~AppState.sidebar_collapsed,
                rx.text(
                    text,
                    style={"color": COLORS["subtext1"]},
                    class_name="font-medium group-hover:text-[#cdd6f4] transition-colors duration-200",
                ),
                rx.fragment(),
            ),
            class_name="gap-3 px-3 py-2.5 rounded-lg group hover:bg-[#313244] transition-all duration-200 w-full",
        ),
        href=href,
        class_name="no-underline",
    )


def sidebar() -> rx.Component:
    """Main sidebar component with Catppuccin Mocha theme."""
    return rx.fragment(
        # Desktop Sidebar
        rx.box(
            rx.vstack(
                # Header
                rx.box(
                    rx.hstack(
                        rx.image(
                            src="/Twinverse.svg",
                            class_name="w-10 h-10 rounded-xl",
                        ),
                        rx.cond(
                            ~AppState.sidebar_collapsed,
                            rx.vstack(
                                rx.text(
                                    "TryOn",
                                    style={"color": COLORS["text"]},
                                    class_name="font-bold text-lg leading-none",
                                ),
                                rx.text(
                                    "Dashboard",
                                    style={"color": COLORS["overlay1"]},
                                    class_name="text-xs leading-none",
                                ),
                                class_name="gap-0.5 items-start",
                            ),
                            rx.fragment(),
                        ),
                        class_name="gap-3 items-center",
                    ),
                    style={"borderColor": COLORS["surface0"]},
                    class_name="px-4 py-5 border-b",
                ),
                # Navigation
                rx.vstack(
                    rx.cond(
                        ~AppState.sidebar_collapsed,
                        rx.text(
                            "MENU",
                            style={"color": COLORS["overlay0"]},
                            class_name="text-xs font-semibold tracking-wider px-3 mb-2",
                        ),
                        rx.fragment(),
                    ),
                    sidebar_link("Dashboard", "/", "layout-dashboard"),
                    sidebar_link("Logs", "/logs", "scroll-text"),
                    class_name="gap-1 w-10 px-3 py-4 flex-1",
                ),
                # Footer
                rx.box(
                    rx.cond(
                        ~AppState.sidebar_collapsed,
                        rx.hstack(
                            rx.image(
                                src="/Twinverse.svg",
                                class_name="w-10 h-10 rounded-xl",
                            ),
                            rx.vstack(
                                rx.text(
                                    "Twinverse",
                                    style={"color": COLORS["text"]},
                                    class_name="text-sm font-medium leading-none",
                                ),
                                rx.text(
                                    "v1.0.0",
                                    style={"color": COLORS["overlay0"]},
                                    class_name="text-xs leading-none",
                                ),
                                class_name="gap-0.5 items-start",
                            ),
                            class_name="gap-3 items-center",
                        ),
                        rx.box(
                            rx.text(
                                "T",
                                style={"color": COLORS["mauve"]},
                                class_name="text-sm font-bold",
                            ),
                            style={"background": COLORS["surface0"]},
                            class_name="w-8 h-8 rounded-full flex items-center justify-center mx-auto",
                        ),
                    ),
                    style={"borderColor": COLORS["surface0"]},
                    class_name="px-4 py-4 border-t",
                ),
                class_name="h-full justify-between",
            ),
            # Collapse toggle button
            rx.button(
                rx.cond(
                    AppState.sidebar_collapsed,
                    rx.icon("chevron-right", size=14, style={"color": COLORS["text"]}),
                    rx.icon("chevron-left", size=14, style={"color": COLORS["text"]}),
                ),
                on_click=AppState.toggle_sidebar,
                style={"background": COLORS["surface0"], "borderColor": COLORS["surface1"]},
                class_name="absolute -right-3 top-7 w-6 h-6 border rounded-full flex items-center justify-center hover:bg-[#45475a] transition-colors cursor-pointer z-10",
                variant="ghost",
                size="1",
            ),
            style={"background": COLORS["mantle"], "borderColor": COLORS["surface0"]},
            class_name=rx.cond(
                AppState.sidebar_collapsed,
                "hidden md:flex flex-col h-screen border-r relative transition-all duration-300 w-20",
                "hidden md:flex flex-col h-screen border-r relative transition-all duration-300 w-fit px-8",
            ),
        ),
        # Mobile overlay
        rx.cond(
            AppState.mobile_sidebar_open,
            rx.box(
                on_click=AppState.close_mobile_sidebar,
                class_name="fixed inset-0 bg-black/60 backdrop-blur-sm z-40 md:hidden",
            ),
            rx.fragment(),
        ),
        # Mobile sidebar
        rx.box(
            rx.vstack(
                # Header
                rx.hstack(
                    rx.image(
                        src="/Twinverse.svg",
                        class_name="w-10 h-10 rounded-xl",
                    ),
                    rx.text(
                        "TryOn Dash",
                        style={"color": COLORS["text"]},
                        class_name="font-bold text-lg",
                    ),
                    style={"borderColor": COLORS["surface0"]},
                    class_name="gap-3 items-center px-4 py-5 border-b w-full",
                ),
                # Navigation
                rx.vstack(
                    sidebar_link("Dashboard", "/", "layout-dashboard"),
                    sidebar_link("Logs", "/logs", "scroll-text"),
                    class_name="gap-1 w-full px-3 py-4 flex-1",
                ),
                class_name="h-full",
            ),
            style={"background": COLORS["mantle"]},
            class_name=rx.cond(
                AppState.mobile_sidebar_open,
                "fixed top-0 left-0 z-50 h-full w-64 shadow-2xl transform transition-transform duration-300 md:hidden translate-x-0",
                "fixed top-0 left-0 z-50 h-full w-64 shadow-2xl transform transition-transform duration-300 md:hidden -translate-x-full",
            ),
        ),
        # Mobile toggle button
        rx.button(
            rx.cond(
                AppState.mobile_sidebar_open,
                rx.icon("x", size=20, style={"color": COLORS["text"]}),
                rx.icon("menu", size=20, style={"color": COLORS["text"]}),
            ),
            on_click=AppState.toggle_mobile_sidebar,
            style={"background": COLORS["surface0"], "borderColor": COLORS["surface1"]},
            class_name="fixed top-4 left-4 z-50 md:hidden p-4 rounded-lg border",
            variant="ghost",
        ),
    )
