"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
from pcconfig import config

import pynecone as pc

docs_url = "https://pynecone.io/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"


class State(pc.State):
    """The app state."""

    pass


def index() -> pc.Component:
    return pc.center(
        pc.vstack(
            pc.heading("Let's get learning Pynecone!", font_size="2em"),
            pc.box("Get started by editing ", pc.code(filename, font_size="1em")),
            pc.text(
                "Root Page",
                color="blue",
                font_size="1.5em"
            ),
            pc.link(
                "Check out our docs!",
                href=docs_url,
                border="0.1em solid",
                padding="0.5em",
                border_radius="0.5em",
                _hover={
                    "color": "rgb(107,99,246)",
                },
            ),
            pc.text(
                "Hello World!",
                color="red",
                font_size="1.5em"
            ),
            pc.hstack(
                pc.circular_progress(
                    pc.circular_progress_label(
                        "50", color="green"
                    ),
                    value=50,
                ),
                pc.circular_progress(
                    pc.circular_progress_label(
                        "∞", color="rgb(107, 99, 246)"
                    ),
                    is_indeterminate=True,
                ),
            ),
            spacing="1.5em",
            font_size="2em",
        ),
        padding_top="10%",
    )

def about():
    return pc.center(
        pc.vstack(
            pc.avatar(
                name="John Doe",
            ),
            pc.text("About Page"),
            pc.button(
                "Fancy Button",
                border_radius="1em",
                box_shadow="rgba(151, 65, 252, 0.8) 0 15px 30px -10px",
                background_image="linear-gradient(144deg,#AF40FF, #5B42F3 50%, #00DDEB)",
                box_sizing="border-box",
                color="white",
                _hover={
                    "opacity": 0.85,
                },
            )
        )
    )

# Add state and page to the app.
app = pc.App(state=State)
app.add_page(index, route="/")
app.add_page(about, route="/about")
app.compile()
