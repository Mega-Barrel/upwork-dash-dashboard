import dash_bootstrap_components as dbc
from utils.dash_navbar import navbar
from dash import html

dashboard = [
    navbar,
    html.Br(),
    dbc.Row(
        dbc.Col(
            html.H3(
                "Dashboard Page", 
                style={"color": "#a3004c", "font-family": "changa"}
            ),
            width=2,
        ),
        className="ml-5 mb-0",
    ),
]

