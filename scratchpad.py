from apikeys import finnhub_api_key
from functions import get_candle
from functions import get_symbols_sheet
from functions import dt_str

import requests
import pytz
from datetime import datetime
from datetime import timezone

from matplotlib import pyplot


start_date = dt_str(datetime(2020,11,25))
end_date = dt_str(datetime(2020,11,26))

print(start_date)
print(end_date)
print("="*80)

# save this to a file and load it rather than pull it everytime
data = get_candle("SPY", start_date, end_date)

print(data)
print("="*80)

data1 = data["c"]
data2 = data["v"]

pyplot.scatter(data1, data2)
pyplot.show()

