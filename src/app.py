# Dash imports:
from dash import Dash, html, dcc
import plotly.express as px

# HTML Layout imports:
from layout import app_layout 

# Callback Imports:
from callbacks.price_timeseries_callbacks import generate_historical_price_timeseries

app  = Dash(__name__)

app.layout = app_layout


if __name__ == "__main__":
    app.run_server(debug=True)