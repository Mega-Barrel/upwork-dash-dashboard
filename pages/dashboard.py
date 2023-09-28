import dash_bootstrap_components as dbc
from utils.dash_navbar import navbar
from dash import html, dcc
import pandas as pd


# Sample data for line chart
df_line = pd.DataFrame(
    {
        'X': [1, 2, 3, 4, 5],
        'Y': [10, 11, 12, 13, 14]
    }
)

# Sample data for pie chart
df_pie = pd.DataFrame(
    {
        'Category': ['A', 'B', 'C'],
        'Values': [30, 45, 25]
    }
)

# Create a list of options for the dropdown menu
dropdown = html.Div(
    [
        dbc.DropdownMenu(
            [
                dbc.Col(
                    dbc.DropdownMenuItem(
                        "Update Chart", id="update-button", n_clicks=0
                    )
                ),
                dbc.Col(
                    dbc.DropdownMenuItem(
                        "Extract data", id="extract-button", n_clicks=0
                    )
                )
            ],
            label="Chart Options",
        ),

        # Optional
        html.P(
            id="item-clicks", 
            className="mt-3"
        ),
    ]
)

dashboard = dbc.Container(
    [
        navbar,
        html.Br(),
        dbc.Row(
            [
                dbc.Col(
                    dbc.Card(
                        [
                            dbc.CardHeader(
                                dbc.Row(
                                    [
                                        dbc.Col(
                                            html.H5("Site Stats"), 
                                            width=6
                                        ),
                                        dbc.Col(
                                            dropdown,
                                            width=6,
                                            style={"textAlign": "right"},
                                        ),  # Button
                                    ],
                                    style={"marginLeft": "0px", "marginRight": "0px"}
                                ),
                            ),
                            dbc.CardBody(
                                [
                                    # Line chart
                                    dcc.Graph(
                                        id='line-chart',
                                        figure={
                                            'data': [
                                                {'x': df_line['X'], 'y': df_line['Y'], 'type': 'line', 'name': 'Line Chart'},
                                            ],
                                            'layout': {
                                                'title': 'Line Chart'
                                            }
                                        },
                                        config={
                                            'displayModeBar': False
                                        },
                                    ),
                                    dcc.Markdown(id="button-output"),
                                ]
                            ),
                        ],
                        className="mb-3"
                    ),
                    width=6,
                    style={"margin-left": "50px"}
                ),
                
                dbc.Col(
                dbc.Card(
                    [
                        dbc.CardHeader(
                            dbc.Row(
                                [
                                    dbc.Col(
                                        html.H5("Devices"), 
                                        width=6
                                    ),
                                    dbc.Col(
                                        dropdown,
                                        width=6,
                                        style={"textAlign": "right"},
                                    ),
                                ],
                                style={"marginLeft": "0px", "marginRight": "0px", "marginBottom": "0px"}
                            ),
                        ),
                        dbc.CardBody(
                            [
                                # Line chart
                                dcc.Graph(
                                    id='pie-chart',
                                    figure={
                                        'data': [
                                            {'labels': df_pie['Category'], 'values': df_pie['Values'], 'type': 'pie', 'name': 'Pie Chart'},
                                        ],
                                        'layout': {
                                            'title': 'Pie Chart'
                                        }
                                    },
                                    config={
                                        'displayModeBar': False
                                    },
                                ),
                                dcc.Markdown(id="button-output"),
                            ]
                        ),
                    ],
                    className="mb-3"
                ),
                width=5,
            )
            ]
        ),
        
        
        
        dbc.Row(
            [
                dbc.Col(
                    dbc.Card(
                        [
                            dbc.CardHeader(
                                dbc.Row(
                                    [
                                        dbc.Col(
                                            html.H5("Site Stats"), 
                                            width=6
                                        ),
                                        dbc.Col(
                                            dropdown,
                                            width=6,
                                            style={"textAlign": "right"},
                                        ),  # Button
                                    ],
                                    style={"marginLeft": "0px", "marginRight": "0px"}
                                ),
                            ),
                            dbc.CardBody(
                                [
                                    # Line chart
                                    dcc.Graph(
                                        id='line-chart',
                                        figure={
                                            'data': [
                                                {'x': df_line['X'], 'y': df_line['Y'], 'type': 'line', 'name': 'Line Chart'},
                                            ],
                                            'layout': {
                                                'title': 'Line Chart'
                                            }
                                        },
                                        config={
                                            'displayModeBar': False
                                        },
                                    ),
                                    dcc.Markdown(id="button-output"),
                                ]
                            ),
                        ],
                        className="mb-3"
                    ),
                    width=6,
                    style={"margin-left": "50px"}
                ),
                
                dbc.Col(
                dbc.Card(
                    [
                        dbc.CardHeader(
                            dbc.Row(
                                [
                                    dbc.Col(
                                        html.H5("Devices"), 
                                        width=6
                                    ),
                                    dbc.Col(
                                        dropdown,
                                        width=6,
                                        style={"textAlign": "right"},
                                    ),
                                ],
                                style={"marginLeft": "0px", "marginRight": "0px", "marginBottom": "0px"}
                            ),
                        ),
                        dbc.CardBody(
                            [
                                # Line chart
                                dcc.Graph(
                                    id='pie-chart',
                                    figure={
                                        'data': [
                                            {'labels': df_pie['Category'], 'values': df_pie['Values'], 'type': 'pie', 'name': 'Pie Chart'},
                                        ],
                                        'layout': {
                                            'title': 'Pie Chart'
                                        }
                                    },
                                    config={
                                        'displayModeBar': False
                                    },
                                ),
                                dcc.Markdown(id="button-output"),
                            ]
                        ),
                    ],
                    className="mb-3"
                ),
                width=5,
            )
            ]
        )
    ],
    fluid=True
)
