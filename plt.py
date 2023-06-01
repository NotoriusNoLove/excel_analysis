from dash import Dash, dcc, html, Input, Output
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html


app = Dash(__name__)

text = """
Grand total of income, and their breakdowns showing the achievements percentage and highlight for most valuable source, Marketing strategies, and operating profit.

"""

app.layout = html.Div([
    html.H1("Fin Stat Dashboard"),
    html.Div(text)
])

if __name__ == '__main__':
    app.run_server(debug=True)
