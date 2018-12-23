import pandas as pd
import datetime

today = datetime.datetime.today().strftime('%Y%m%d')
url = f"https://coinmarketcap.com/currencies/ravencoin/historical-data/?start=20130428&end={today}"

# historical = pd.read_html(url, parse_dates=['Date'], index_col=0)[0]
historical = pd.read_html(url, parse_dates=['Date'])[0]

# with pd.option_context('display.max_rows', None, 'display.max_columns', None):
#     # print(historical['Close**'])
#     print(historical['Date'])

path = r"C:\Users\Pat\Desktop\Raven\Ravencoin-FMV-master\export.csv"
export = pd.read_csv(path, usecols=['Date', 'Type', 'Label', 'Amount (RVN)'], parse_dates=['Date'])
# export['Date'] = export['Date'].dt.strftime('%Y-%m-%d')
export['Date'] = pd.to_datetime(export['Date'].dt.strftime('%Y-%m-%d'), format='%Y-%m-%d')
# with pd.option_context('display.max_rows', None, 'display.max_columns', None):
#     # print(export)
#     print(export['Date'])
# header = ['Date', 'Type', 'Label', 'Amount (RVN)', 'Fair Market Value', 'Capital Asset']

# export['Fair Market Value'] = export['Amount (RVN)'].mul(historical[])
# export['Capital Asset'] = export['Amount (RVN)'] * export['Fair Market Value']

export = pd.merge(left=export, right=historical[['Date', 'Close**']], how='left', on=['Date'])
export['Capital Asset (USD)'] = export['Amount (RVN)'] * export['Close**']
export.rename(columns={'Close**': 'FMV (USD)'}, inplace=True)
export = export.iloc[::-1].reset_index(drop=True)
export.to_csv(path.rstrip('export.csv') + 'output.csv')

summary = export.groupby(export['Date'].dt.strftime('%Y')).sum()
summary.index.names = ['Year']
summary.to_csv(path.rstrip('export.csv') + 'summary.csv')
with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    print(summary)
