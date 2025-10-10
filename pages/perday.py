import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import dash_ag_grid as dag
import pandas as pd
import plotly.express as px

dash.register_page(__name__)

companies = ["blackberry", "electrolux", "zyxel", "daewoo", "cybex"]

selectable_companies = [
    "adidas",
    "arg",
    "artel",
    "atlant",
    "beko",
    "blackberry"
    "brw",
    "casio",
    "cybex",
    "daewoo",
    "dell",
    "dinastia",
    "dji",
    "electrolux",
    "garmin",
    "giant",
    "haier",
    "honor",
    "janome",
    "karcher",
    "ledi",
    "midea",
    "msi",
    "oneplus",
    "philips",
    "phoenix",
    "rals",
    "robertobravo",
    "smeg",
    "sokolov",
    "sv",
    "tefal",
    "uta",
    "vivo",
    "zyxel", 
]
df = pd.read_csv("Dta/agg/brnd_per_day_sales_all.csv")
flt = df[df["brand"].isin(companies)]

fig = px.line(flt, x="date", y="price", color="brand")

columnDefs = [
    {"field": "date"},
    {"field": "brand", "headerName": "Company"},
    {"field": "price", "headerName": "Sales total"},
]

grid = dag.AgGrid(
    id="getting-started-headers",
    rowData=flt.to_dict("records"),
    columnDefs=columnDefs,
    defaultColDef={"filter": True},
    dashGridOptions={"pagination": True, "paginationPageSize": 100},
    # dashGridOptions={"animateRows": False}
)


layout = html.Div(
    [
        html.H2("Daily Sales Analysis"),
        dcc.Dropdown(
            id="controls-and-check-item-gkvh",
            options=selectable_companies,
            value=companies,
            multi=True,
        ),
        dcc.Graph(figure=fig),
        grid,
    ]
)
