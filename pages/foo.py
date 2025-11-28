# Sitzungsverfolgung
from dash import Dash, html, dash_table, dcc, callback, Output, Input, register_page
import plotly.express as px
import pandas as pd
import dash_ag_grid as dag
    
from sba.dd import DD
    
sub_title = "Test"

register_page(__name__)

 
layout = html.Div(
    [
        html.H3(sub_title),
        
    ]
)
