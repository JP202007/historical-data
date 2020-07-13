import requests
import pandas as pd
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 1000)
#
curs={'node','lol','akt','tt','btc'}

coins={"usdt","eth","btc","husd"}


for cur in curs:
  for coin in coins:
      symbol=cur+coin
      url = "https://api.huobi.br.com/market/history/kline?period=1day&size=500&symbol="+symbol

      print(url)
      resp=requests.get(url)
      resp_json = resp.json()
      resp_status=resp_json['status']

      if resp_status=='error':
         print('none')
      else:
        data_list = resp_json['data']
        df = pd.DataFrame(data_list)
        df['market_name'] = cur+'-'+coin

        df.to_csv(symbol + '.csv')
        print(df)
