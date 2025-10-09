import dash
from dash import html, dcc
from dash.dependencies import Input, Output

dash.register_page(__name__, path='/')

layout = html.Div([
    html.H2('Willkommen auf der Startseite'),
    dcc.Markdown('''
       Text folgt ...
    ''')
])