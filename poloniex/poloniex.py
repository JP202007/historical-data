import requests
import pandas as pd
pd.set_option('expand_frame_repr', False)

curs={'JST'}
coins={"_USDT","_ETH","_BTC","_TRX","_USDC"}

for cur in curs:
    for coin in coins:
        symbol = cur+coin
        url = 'https://poloniex.com/public?command=returnChartData&currencyPair='+symbol\
              +'&start=1546300800&end=1589414400&period=86400'

        print(url)
        resp = requests.get(url)
        data = resp.json()

        if len(data) > 1:

            df = pd.DataFrame(data)
            df['market_name'] = symbol
            df.to_csv(symbol + '.csv')
            print(df)
        else:
            print('none')


