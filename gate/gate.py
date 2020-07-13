import requests
import pandas as pd
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 1000)
#
curs={'kai','dili','vidy','sero','gmat','mbl','drep','cnns','btc'}

coins={"_usdt","_eth","_btc"}


for cur in curs:
  for coin in coins:
      symbol=cur+coin
      url = "https://data.gateio.la/api2/1/candlestick2/"+symbol+"?group_sec=86400&range_hour=17000"

      print(url)
      resp=requests.get(url)
      resp_json = resp.json()
      resp_status=resp_json['result']

      if resp_status=='false':
         print('none')
      else:
        data_list = resp_json['data']
        df = pd.DataFrame(data_list,columns={'time': 0, 'volume': 1, 'close': 2, 'high': 3, 'low': 4, 'open': 5})
        df['market_name'] = cur+'-'+coin

        df.to_csv(symbol + '.csv')
        print(df)
