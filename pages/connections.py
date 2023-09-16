import dash_bootstrap_components as dbc
from utils.dash_navbar import navbar
from dash import html

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
            width=2,
        ),
        className="ml-5 mb-0",
    ),

    html.Br(),

    dbc.Row(
        html.H2(
            "Your Connections", 
            style={
                "color": "#a3004c", 
                "font-family": "changa"
            }
        ),
        className="ml-5 mb-0",
    ),
    
    dbc.Row(
        [
            dbc.Col(
                dbc.Card(
                    dbc.CardBody(
                        [
                            html.H4('Simple Analytics API'),
                            html.P('Created on September 16, 2023 9:32 PM')
                        ]
                    ),
                    className="mb-3"
                ),
                width=6,
                style={"margin-left": "50px"}   
            )
        ]
    ),

    html.Br()
]

