from dash import Dash
from dash.long_callback import DiskcacheLongCallbackManager
import dash_bootstrap_components as dbc

# -----------------------------------------APP DEFINITION---------------------------------------------------------------
FONT_AWESOME = (
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css"
)
CARD_STYLE = "https://fonts.googleapis.com/css?family=Saira+Semi+Condensed:300,400,700"

## Diskcache
import diskcache

cache = diskcache.Cache("./cache")
long_callback_manager = DiskcacheLongCallbackManager(cache)

app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP, FONT_AWESOME, CARD_STYLE],
    long_callback_manager=long_callback_manager,
    suppress_callback_exceptions=True,
)

app.title = "Chartbrew - Visualize your data in one place"