import dash_bootstrap_components as dbc
from dash import html
import dash_trich_components as dtc

# SIDEBAR_STYLE = {
#     "position": "fixed",
#     "top": 62.5,
#     "left": 0,
#     "bottom": 0,
#     "width": "16rem",
#     "height": "100%",
#     "z-index": 1,
#     "overflow-x": "hidden",
#     "transition": "all 0.5s",
#     "padding": "0.5rem 1rem",
#     "background-color": "#f8f9fa",
# }

# sidebar = html.Div(
#     [
#         html.P('Website Stats'),
#         html.Hr(),

#         dbc.Nav(
#             [
#                 dbc.NavLink(
#                     'Connections',
#                     href='/pages/connections.py',
#                     id='connections-link'
#                 ),
#                 dbc.NavLink(
#                     'Project Settings',
#                     href='/pages/project_settings.py',
#                     id='project-settings-link'
#                 )
#             ],
#             vertical=True,
#             pills=True
#         ),

#         html.Hr(),

#         html.P('Chatbrew 2.9.0')
#     ],
#     id='sidebar',
#     style=SIDEBAR_STYLE
# )

sidebar = html.Div(
    [
        dtc.SideBar(
            [
                
                dtc.SideBarItem(
                    id="dashboard",
                    label="Dashboard",
                    icon="fa-solid fa-chart-line",
                    className="h1"
                ),
                dtc.SideBarItem(
                    id="connections",
                    label="Connections",
                    icon="fa-solid fa-plug",
                    className="h1",
                ),
                dtc.SideBarItem(
                    id="dashboard_report",
                    label="Dashboard Report",
                    icon="fa-solid fa-chart-pie",
                    className="h1",
                ),
                dtc.SideBarItem(
                    id="project_settings",
                    label="Project Settings",
                    icon="fa-solid fa-diagram-project",
                    className="h1",
                ),
                
                html.Div(
                    html.P(
                        'Team',
                        className="SidebarP"
                    )
                ),
                dtc.SideBarItem(
                    id="members", 
                    label="Members", 
                    icon="fa-solid fa-user-plus", 
                    className="h1"
                ),
                dtc.SideBarItem(
                    id='integrations',
                    label="Integrations",
                    icon='fa-solid fa-screwdriver-wrench',
                    className="h1"
                ),
                dtc.SideBarItem(
                    id='settings',
                    label="Settings",
                    icon='fa-solid fa-gear',
                    className="h1"
                )
            ],
            bg_color="#080808",
            text_color="#1a7fa0",
            className="sidebar"
        ),
        html.Div(
            [], 
            id="page_content"
        ),
    ],
    style={"position": "relative"},
)

# import dash_trich_components as dtc
# from dash.dependencies import Input, Output
# import pandas as pd

# content_1 = html.Div('content 1')
# content_2 = html.Div('content 2')
# content_3 = html.Div('content 3')
# content_4 = html.Div('content 4')
# content_5 = html.Div('content 5')

# sidebar = html.Div(
#     [
#     dtc.SideBar(
#         [
#             dtc.SideBarItem(id='id_1', label="Label 1", icon="fas fa-home"),
#             dtc.SideBarItem(id='id_2', label="Label 2", icon="fas fa-chart-line"),
#             dtc.SideBarItem(id='id_3', label="Label 3", icon="far fa-list-alt"),
#             dtc.SideBarItem(id='id_4', label="Label 4", icon="fas fa-info-circle"),
#             dtc.SideBarItem(id='id_5', label="Label 5", icon="fas fa-cog"),
#         ]
#     ),
#     html.Div(
#         [
#     ], id="page_content"),
# ])

