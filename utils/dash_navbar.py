import dash_bootstrap_components as dbc
from dash import html, dcc

PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"

# make a reuseable navitem for the different examples
nav_item_help = dbc.NavItem(
    dbc.NavLink(
        "Link", 
        href="#"
    )
)

nav_item_update = dbc.NavItem(
    dbc.NavLink(
        "Updates",
        href="#"
    )
)

nav_item_settings = dbc.NavItem(
    dbc.NavLink(
        "Settings", 
        href="#"
    )
)

# Navbar layout
navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(
                            html.Img(
                                src=PLOTLY_LOGO,
                                height="30px"
                            ),
                            style={"marginLeft": "-100%"}
                        ),
                        dbc.Col(
                            dbc.NavbarBrand(
                                "chartbrew.com",
                                className="ms-2"
                            ),
                            style={"marginLeft": "-80%"}
                        ),
                    ],
                    align="center",
                    className="g-0",
                ),
                href="https://plotly.com",
                style={"textDecoration": "none"},
                className="me-auto"
            ),


            dbc.NavbarToggler(id="navbar-toggler2", n_clicks=0),
            dbc.Collapse(
                dbc.Nav(
                    [
                        nav_item_update, 
                        nav_item_help, 
                        nav_item_settings
                    ],
                    className="ms-auto",
                    navbar=True,
                    style={"marginRight": "-13%"}
                ),
                id="navbar-collapse2",
                navbar=True,
            ),
        ],
    ),
    color="white",
    dark=False,
    className="mb-5",
    sticky='top',
)