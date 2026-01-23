"""TryOn Dashboard - Reflex Application."""

import reflex as rx

from .state import AppState
from .pages.dashboard import dashboard_page
from .pages.logs import logs_page


# Create the app
app = rx.App(
    theme=rx.theme(
        appearance="light",
        accent_color="indigo",
        radius="medium",
    ),
)

# Add pages
app.add_page(dashboard_page, route="/", title="Dashboard | TryOn")
app.add_page(logs_page, route="/logs", title="Logs | TryOn")
