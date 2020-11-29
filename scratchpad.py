from apikeys import finnhub_api_key
from functions import get_candle
from functions import get_symbols_sheet
from functions import dt_str

import requests
import pytz
from datetime import datetime
from datetime import timezone



#start_date = "1605537000"
#end_date = "1605537060"
#ny_tz = pytz.timezone('US/Eastern')
#start_date = ny_tz.localize(datetime(2020,11,2,9,30))
#end_date = ny_tz.localize(datetime(2020,11,3))
#start_date_ts = str(int(start_date.replace().timestamp()))
#end_date_ts = str(int(end_date.replace().timestamp()))

#spy = get_candle("SPY", start_date, end_date, "D")
start_date = dt_str(datetime(2020,11,25,9,30))
end_date = dt_str(datetime(2020,11,25,9,31))

print(start_date)
print(end_date)

print(get_candle("SPY", start_date, end_date))



# symbol = "SPY"

# spy = requests.get('https://finnhub.io/api/v1/stock/candle?symbol=' + symbol + '&resolution=1&from=' + start_date + '&to=' + end_date + '&token=' + finnhub_api_key)

#print(spy.json().values())


