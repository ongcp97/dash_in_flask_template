from dash import dcc, html, Output, Input, State
def create_layout():
    layout = html.Div([
        html.Div(id='dash-page-content'),
        dcc.Location(id='dash-url'),
    ])

    return layout
