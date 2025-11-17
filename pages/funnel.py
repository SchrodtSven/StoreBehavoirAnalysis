from dash import Dash, html, dash_table, dcc, callback, Output, Input, register_page
import plotly.express as px
import pandas as pd
import dash_ag_grid as dag

register_page(__name__)

sub_title = "🔄 Funnel Analysis"

df = pd.read_csv("Dta/agg/funnel_all.csv")
fig = px.funnel(df, x="date", y="count", color="evt")

colz = ["date", "count", "evt"]

layout = html.Div(
    [
        html.Div(
            [
                html.H1(
                    "Session Analysis",
                    
                ),
                html.P(
                    "Funnel stuff    ",
                    
                ),
            ],
        ),
        html.Div(
            [
                html.Div(
                    [
                        html.H4(
                            "Funnel Vis.",
                        ),
                        dcc.Graph(
                            figure=fig,
                            id="funnel-controls-and-graph",
                            
                        ),
                    ],
                    style={"marginBottom": "30px"},
                ),
                # Daterange Slider
                dcc.DatePickerRange(
                    id="my-date-picker-range",
                    min_date_allowed=df["date"].min(),
                    max_date_allowed=df["date"].max(),
                ),
                # Data Grid Section
                html.Div(
                    [
                        html.H4(
                            "Data",
                            
                        ),
                        dag.AgGrid(
                            id="main_grid_basic",
                            rowData=df.to_dict("records"),
                            columnDefs=[
                                {
                                    "field": x,
                                    "headerName": x,
                                    "filter": True,
                                    "sortable": True,
                                }
                                for x in colz
                            ],
                            columnSize="responsiveSizeToFit",
                            dashGridOptions={
                                "pagination": True,
                                "paginationPageSize": 15,
                                "animateRows": True,
                            },
                        ),
                    ]
                ),
            ],
        ),
    ],
    
)
