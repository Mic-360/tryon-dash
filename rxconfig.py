import reflex as rx

config = rx.Config(
    app_name="tryon_dash",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)