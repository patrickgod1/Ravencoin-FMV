import pandas as pd
import datetime
import os.path


def updateHistoricalData(currentDate, cwd):
    url = f"https://coinmarketcap.com/currencies/ravencoin/historical-data/?start=20130428&end={currentDate}"
    historical = pd.read_html(url, parse_dates=['Date'])[0]
    historical.to_csv(f'{cwd}\\historicalData.csv')


def main():
    cwd = os.path.dirname(os.path.abspath(__file__))
    today = datetime.datetime.utcnow().strftime('%Y%m%d')
    if os.path.isfile('historicalData.csv'):
        historical = pd.read_csv(f'{cwd}\\historicalData.csv', parse_dates=['Date'])
        if(historical.iloc[0]['Date'] < datetime.datetime.strptime(today, '%Y%m%d')):
            updateHistoricalData(today, cwd)
    else:
        updateHistoricalData(today, cwd)

    export = pd.read_csv(f'{cwd}\\export.csv', usecols=['Date', 'Type', 'Label', 'Amount (RVN)'], parse_dates=['Date'])
    export['Date'] = pd.to_datetime(export['Date'].dt.strftime('%Y-%m-%d'), format='%Y-%m-%d')

    export = pd.merge(left=export, right=historical[['Date', 'Close**']], how='left', on=['Date'])
    export['Capital Asset (USD)'] = export['Amount (RVN)'] * export['Close**']
    export.rename(columns={'Close**': 'FMV (USD)'}, inplace=True)
    export = export.iloc[::-1].reset_index(drop=True)
    export.to_csv(f'{cwd}\\output.csv')

    summary = export[['Date', 'Type', 'Label', 'Amount (RVN)', 'Capital Asset (USD)']].groupby(export['Date'].dt.strftime('%Y')).sum()
    summary.index.names = ['Year']
    summary.to_csv(f'{cwd}\\summary.csv')
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):
        print(summary)


if __name__ == "__main__":
    main()
