# Dash imports:
from dash import html, dcc

# Utility method imports:
from utils.ticker_selection import populate_ticker_dropdown

app_layout = html.Div([

    # Main input field for ticker:
    dcc.Dropdown(options=populate_ticker_dropdown(), id="ticker_seletor_dropdown", placeholder="Ticker Symbol"),

    # Historical Price Timeseries Graph:
    dcc.Graph(id="hisorical_price_timeseries")

])