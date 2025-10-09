# Factory Klasse für Tab-Content
#
# AUTHOR Sven Schrodt
# SINCE 2025-10-07

# 3rd party libs
from dash import (
    Dash,
    html,
    page_registry,
    page_container,
    clientside_callback,
    Input,
    Output,
    callback,
    dcc,
    Patch,
)
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template
import dash
import dash_ag_grid as dag
import pandas as pd
import plotly.express as px

# Projekteigene Module
from dd import DD


class TabFactory:
    """Factory for content of tab's children
    - dataframes
    - grids
    - graphs
    - tbd.
    """

    pass

    @staticmethod
    def df(ds: str, dt: str) -> pd.DataFrame:
        """Getting dataframe from given data source"""
        df = pd.read_csv(ds)
        df[dt] = pd.to_datetime(df[dt], format="%Y-%m-%d")
        return df
        # print(ds, dt)
        # exit(23)

    @staticmethod
    def generic(ds: str) -> html.Div:
        # load data source
        # opt. grid
        # opt. graphs
        pass

    @staticmethod
    def grid():
        pass

    @staticmethod
    def sales():
        colz = [
            "Bestellungen",
            "Bruttoumsatz",
            "Rabatte",
            "Rückgaben",
            "Nettoumsatz",
            "Versandgebühren",
            "Steuern",
            "Gesamtumsatz",
        ]
        strt_colz = ["Nettoumsatz"]
        df = TabFactory.df("output/sales_per_channel.csv", "Tag")
        fig = px.line(df, x="Tag", y=strt_colz, color="Vertriebskanal")
        opt = [{"label": k, "value": k} for k in colz]

        return html.Div(
            [
                html.H3("Umsatz nach Vertiebskanal"),
                html.Div(
                    className="custom-dropdown-style",
                    children=[
                        dcc.Dropdown(
                            id="sales-sales-controls-and-check-item",
                            options=opt,
                            value=strt_colz,
                            multi=True,
                            className="dropdown-class",
                            style={"background-color": "#011213"},
                        )
                    ],
                ),
                dcc.Graph(figure=fig, id="sales-sales-controls-and-graph"),
                dag.AgGrid(
                    id="main_grid_basic",
                    rowData=df.to_dict("records"),
                    columnDefs=[{"field": x, "headerName": x} for x in colz],
                    columnSize="responsiveSizeToFit",
                    dashGridOptions={"pagination": True},
                ),
            ]
        )


# d = TabFactory.df()
# print(d.dtypes)

if __name__ == "__main__":
     print(help(TabFactory))