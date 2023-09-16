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

# graph options
# graph_options = [
#     html.Div(
#         [
#             html.Label(['Choose a graph:'],style={'font-weight': 'bold'}),
#             dcc.Dropdown(
#                 id='dropdown',
#                 options=[
#                     {'label': 'refresh chart', 'value': 'chart refresh'},
#                     {'label': 'Export Data to Excel', 'value': 'data download'},
#                     {'label': 'Delete chart', 'value': 'delete chart'}
#                 ],
#                 value='graph1',
#                 style={"width": "60%"}
#             )
#         ]
#     )
# ]

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
    
    dbc.Row(
        [
            dbc.Col(
                dbc.Card(
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
                            )
                        ]
                    ),
                    className="mb-3"
                ),
                width=6,
                style={"margin-left": "50px"}
            ),

            dbc.Col(
                dbc.Card(
                    dbc.CardBody(
                        [
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
                                }
                            )
                        ]
                    ),
                    className="mb-3"
                ),
                width=5
            )
        ]
    )
]

