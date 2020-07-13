import time
import requests
import pandas as pd
pd.set_option('expand_frame_repr', False)

curs=['evt','eved','und','btc','eth']

coins=["eth-","btc-",'usdt-']

for cur in curs:
    for coin in coins:
      symbol= coin+cur

      url='https://api.bitforex.com/api/v1/market/kline?symbol=coin-'+coin+cur+'&ktype=1day&size=600'
      print(url)
      resp=requests.get(url)
      data = resp.json()
      #data_success=data['success']
      if 'message' in data:

          print('none')

      else:
        data_list=data['data']
        df = pd.DataFrame(data_list)
        df['market_name'] = symbol

        df.to_csv(symbol + '.csv')
        print(df)
      time.sleep(20)

