import reflex as rx

config = rx.Config(
    app_name="caliper",
    db_url="sqlite:///reflex.db",
    env=rx.Env.DEV,
)
