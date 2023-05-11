import dash
import warnings
import dash_bootstrap_components as dbc
from flask import Flask
from dash import Dash, dcc, html, Input, Output, State

app = Dash(
    title='heroku-sample',
    suppress_callback_exceptions=True,
    prevent_initial_callbacks=True
)

alerts = html.Div(
    [
        dbc.Alert(
            [
                "This is a primary alert with an ",
                html.A("example link", href="#", className="alert-link"),
            ],
            color="primary",
        ),
        dbc.Alert(
            [
                "This is a danger alert with an ",
                html.A("example link", href="#", className="alert-link"),
            ],
            color="danger",
        ),
    ]
)
app.layout = dbc.Container(
    [
        alerts
    ],
    fluid=True,
)

server = app.server

if __name__ == '__main__':
    app.run_server(debug=True)