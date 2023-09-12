import dash_bootstrap_components as dbc
from utils.dash_navbar import navbar
from dash import html, dcc

connection = [
    navbar,
    html.Br(),
    dbc.Row(
        dbc.Col(
            html.Button(
                'Add a new connection', 
                id='submit-val', 
                n_clicks=0
            ),
            # html.H3(
            #     "Connections Page", 
            #     style={"color": "#a3004c", "font-family": "changa"}
            # ),
            width=2,
        ),
        className="ml-5 mb-0",
    ),

    html.Br(),

    dbc.Row(
        dbc.Col(
            html.H2(
                "Your Connections", 
                style={
                    "color": "#a3004c", 
                    "font-family": "changa"
                }
            ),
            width=2,
        ),
        className="ml-5 mb-0",
    ),

    html.Br()
]

