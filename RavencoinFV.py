import pandas as pd
import datetime

today = datetime.datetime.today().strftime('%Y%m%d')
url = f"https://coinmarketcap.com/currencies/ravencoin/historical-data/?start=20130428&end={today}"

df = pd.read_html(url, header=0, index_col=0)[0]
with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    print(df['Close**'])
