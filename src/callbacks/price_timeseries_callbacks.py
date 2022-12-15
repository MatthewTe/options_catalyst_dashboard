# Importing Dash methods:
import dash
from dash import Input, Output
from dash.exceptions import PreventUpdate

# Graphing methods:
import plotly.express as px

# Data management packages:
import pandas as pd
import yfinance as yf

    
# Callback that generates the historical price data of a company given its ticker:
@dash.callback(
    Output("hisorical_price_timeseries", "figure"),
    Input("ticker_seletor_dropdown", "value")
)
def generate_historical_price_timeseries(ticker: str):
    """
    """
    # Lazy way to ensure that callback does not fire when no ticker is selected.
    if ticker is None:
        raise PreventUpdate

    # Querying yfinance api for historical price data:
    df = yf.Ticker(ticker).history(period="max")

    # Generating timeseries figure based on ticker symbol:
    fig = px.line(df, x=df.index, y="Close")

    return fig