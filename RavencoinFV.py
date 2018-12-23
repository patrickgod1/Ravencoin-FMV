import pandas as pd
import datetime

today = datetime.datetime.today().strftime('%Y%m%d')
url = f"https://coinmarketcap.com/currencies/ravencoin/historical-data/?start=20130428&end={today}"

df = pd.read_html(url)
print(df)
