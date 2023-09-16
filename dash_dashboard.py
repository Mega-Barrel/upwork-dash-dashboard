import pandas as pd
from app import ( app )
from dash import ( html, Input, Output )

from pages import (
    connections as cp,
    dashboard as dp,
    dashboard_and_report as dar,
    project_settings as ps
)

from utils import ( 
    dash_sidebar as ds
)

# Page layout
app.layout = html.Div(
    [
        # dn.navbar,
        ds.sidebar,
        html.Div(
            id="empty-div"
        )
    ],
    style={
        # "backgroundColor": "white",
        "padding": 0,
        "max-width": "100%",
        "min-height": "100%",
        "overflow-x": "hidden",
        "overflow-y": "hidden",
    }
)
# Side bar navigation callback
@app.callback(
    Output("page_content", "children"),
    [
        Input("dashboard", "n_clicks_timestamp"),
        Input("connections", "n_clicks_timestamp"),
        Input("dashboard_report", "n_clicks_timestamp"),
        Input("project_settings", "n_clicks_timestamp"),
        Input("members", "n_clicks_timestamp"),
        Input("integrations", "n_clicks_timestamp"),
        Input("settings", "n_clicks_timestamp")
    ]
)

# @app.callback(
#     Output("page_content", "children"),
#     [
#         Input("id_1", "n_clicks_timestamp"),
#         Input("id_2", "n_clicks_timestamp"),
#         Input("id_3", "n_clicks_timestamp"),
#         Input("id_4", "n_clicks_timestamp"),
#         Input("id_5", "n_clicks_timestamp")
#     ]
# )


def toggle_collapse(input1, input2, input3, input4, input5, input6, input7):
    btn_df = pd.DataFrame(
        {
            "input1": [input1],
            "input2": [input2],
            "input3": [input3],
            "input4": [input4],
            "input5": [input5],
            "input6": [input6],
            "input7": [input7],
        }
    )    
    btn_df = btn_df.fillna(0)

    if btn_df.idxmax(axis=1).values == "input1":
        return dp.dashboard
    if btn_df.idxmax(axis=1).values == "input2":
        return cp.connection
    if btn_df.idxmax(axis=1).values == "input3":
        return dar.dashboard_and_report
    if btn_df.idxmax(axis=1).values == "input4":
        return ps.project_settings
    if btn_df.idxmax(axis=1).values == "input5":
        return 'content_5'

# @app.callback(
#     Output("page_content", "children"),
#     [
#         Input("id_1", "n_clicks_timestamp"),
#         Input("id_2", "n_clicks_timestamp"),
#         Input("id_3", "n_clicks_timestamp"),
#         Input("id_4", "n_clicks_timestamp"),
#         Input("id_5", "n_clicks_timestamp")
#     ]
# )

# def toggle_collapse(
#     input1, input2, input3, input4, input5
# ):
#     btn_df = pd.DataFrame({"input1": [input1], "input2": [input2],
#                            "input3": [input3], "input4": [input4], 
#                            "input5": [input5]})
    
#     btn_df = btn_df.fillna(0)

#     if btn_df.idxmax(axis=1).values == "input1":
#         return dp.dashboard
#     if btn_df.idxmax(axis=1).values == "input2":
#         return cp.connection
#     if btn_df.idxmax(axis=1).values == "input3":
#         return 'content_3'
#     if btn_df.idxmax(axis=1).values == "input4":
#         return 'content_4'
#     if btn_df.idxmax(axis=1).values == "input5":
#         return 'content_5'

if __name__ == "__main__":
    app.run_server(
        debug = False, 
        port = 8080
    )
