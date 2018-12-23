import pandas as pd
import datetime

today = datetime.datetime.today().strftime('%Y%m%d')
url = f"https://coinmarketcap.com/currencies/ravencoin/historical-data/?start=20130428&end={today}"

historical = pd.read_html(url)[0]
with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    print(historical['Close**'])

path = r"C:\Users\Pat\Desktop\Raven\Ravencoin-FMV-master\export.csv"
export = pd.read_csv(path, usecols=['Date', 'Type', 'Label', 'Amount (RVN)'])

with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    print(export)

header = ['Date', 'Type', 'Label', 'Amount (RVN)', 'Fair Market Value', 'Capital Asset']
