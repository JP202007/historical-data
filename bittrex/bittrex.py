import requests
import time
import pandas as pd
import os
pd.set_option('expand_frame_repr', False)

curs=['OCEAN','VBK']
coins=["-USD","-BTC"]

for cur in curs:
    for coin in coins:
        symbol = cur+coin
        url = 'https://api.bittrex.com/v3/markets/'+symbol\
              +'/candles?candleInterval=DAY_1/historical/'
        #/markets/{marketSymbol}/candles/{candleInterval}/historical/{year}/{month}/{day}

        print(url)
        resp = requests.get(url)
        data = resp.json()

        if len(data) >1:
            df = pd.DataFrame(data)
            df['market_name'] = symbol
            df.to_csv(symbol + '1.csv')
            #df.to_csv(symbol + '.csv')

            print(df)
        else:
            print('none')
        time.sleep(2)

