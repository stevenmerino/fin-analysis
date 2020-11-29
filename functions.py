from apikeys import *
import requests
import pandas as pd
import pytz
from datetime import datetime
from datetime import timezone

# Get Open, High, Low, Close, Volume data between a timeframe
def get_candle(symbol="", start_date="", end_date="", resolution="1", api_key=finnhub_api_key):
    r = requests.get("https://finnhub.io/api/v1/stock/candle?symbol=" + symbol + "&resolution=" + resolution + "&from=" + start_date + "&to=" + end_date + "&token=" + api_key)
    return r.json()

# Get Output list of symbols available for an exchange. Available exchanges: https://docs.google.com/spreadsheets/d/1I3pBxjfXB056-g_JYf_6o3Rns3BV2kMGG1nCatb91ls/edit#gid=0
def get_symbols_sheet(exchange="US"):
    r = requests.get("https://finnhub.io/api/v1/stock/symbol?exchange=" + exchange + "&token=" + finnhub_api_key)
    df = pd.DataFrame.from_dict(r.json())
    df.to_excel(exchange + "_symbols.xlsx")

# Localize input dt to US Eastern timezone and output as string    
def dt_str(dt):
    ny_tz = pytz.timezone('US/Eastern')
    ny_date = ny_tz.localize(dt)
    ts = str(int(ny_date.replace().timestamp()))
    return ts
