import requests
import time
import pandas as pd
pd.set_option('expand_frame_repr', False)


curs={'UOS','AMPL'}
coins={"UST","ETH","BTC","USD","EUR","GBP","JPY"}

for cur in curs:
    for coin in coins:
        symbol = cur+coin
        url = 'https://api-pub.bitfinex.com/v2/candles/trade:1D:t'+symbol+'/hist?limit=1000'
        print(url)
        resp = requests.get(url)
        data = resp.json()

        df = pd.DataFrame(data, columns={'time': 0, 'open': 1, 'close': 2, 'high': 3, 'low': 4, 'volume': 5})

        if len(df) > 0:
           df['market_name']=symbol
           df.to_csv(symbol + '.csv')
           print(df)
        else:
          print('none')


