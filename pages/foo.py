# Sitzungsverfolgung
from dash import Dash, html, dash_table, dcc, callback, Output, Input, register_page
import plotly.express as px
import pandas as pd
import dash_ag_grid as dag
    
from sba.dd import DD
    
sub_title = "Test"

# df = pd.read_csv('output/sales_per_channel.csv')
# df['Tag'] = pd.to_datetime(df['Tag'], format='%Y-%m-%d')


# colz = ["Bestellungen","Bruttoumsatz","Rabatte","Rückgaben","Nettoumsatz","Versandgebühren","Steuern","Gesamtumsatz"]
# strt_colz = ["Nettoumsatz"]
 
# opt = [{"label": k, "value": k} for k in colz]
 
# fig = px.line(df, x="Tag", y=strt_colz, color='Vertriebskanal')


register_page(__name__)

 
# @callback(
#     Output(component_id="sales-sales-controls-and-graph", component_property="figure"),
#     Input(component_id="sales-sales-controls-and-check-item", component_property="value"),
# )
# def update_graph(col_chosen):
#     fig = px.line(df, x="Tag", y=col_chosen, title=sub_title, color='Vertriebskanal')
 
#     return fig


layout = html.Div(
    [
        html.H3(sub_title),
        
        # html.Div(className='custom-dropdown-style', children=[dcc.Dropdown(
        #     id="sales-sales-controls-and-check-item",
        #     options=opt,
        #     value=strt_colz,
        #     multi=True,
        #     className='dropdown-class',
        #     style={'background-color':'#011213'}
        # )]),
        # dcc.Graph(figure=fig, id="sales-sales-controls-and-graph"),
        # dag.AgGrid(
        #     id="main_grid_basic",
        #     rowData=df.to_dict("records"),
        #     columnDefs=[
        #         {"field": x, "headerName": x}
        #         for x in colz
        #     ],  
        #     columnSize="responsiveSizeToFit",
        #     dashGridOptions={"pagination": True},
        # ),
        
    ]
)
