"""Layout component for the app with Catppuccin Mocha theme."""

import reflex as rx
from .sidebar import sidebar


# Catppuccin Mocha colors
COLORS = {
    "base": "#1e1e2e",
    "crust": "#11111b",
}


def layout(content: rx.Component) -> rx.Component:
    """Main layout wrapper with sidebar."""
    return rx.hstack(
        sidebar(),
        rx.box(
            content,
            style={"background": COLORS["base"]},
            class_name="flex-1 overflow-y-auto min-h-screen",
        ),
        class_name="w-full",
    )
