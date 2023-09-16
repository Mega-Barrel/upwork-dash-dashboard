import dash_bootstrap_components as dbc
from dash import html
import dash_trich_components as dtc

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
