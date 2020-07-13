import requests
import pandas as pd

pd.set_option('expand_frame_repr', False)

curs=['808TA','BXC','CVA','BCAS','NCI','SXC','HNT','GCZ','BZO','TCZ','NT','FDT','VD']

coins=["USDT","ETH","BTC","VD"]

for cur in curs:
  for coin in coins:
      symbol = cur + coin
      url = "https://api.vindax.com/api/v1/klines?"+"symbol="+symbol+"&interval=1d"

      print(url)
      resp=requests.get(url)
      data = resp.json()
      df = pd.DataFrame(data,columns={'open_time': 0, 'open': 1, 'high': 2, 'low': 3, 'close': 4, 'volume': 5,
                                    'close time': 6,'Quote asset volume':7,'Number of trades':8,
                                  'oth':9,'null':10,'other':11})

      if len(df) > 0:
            #df.set_index('open_time', inplace=True)
            df['market_name'] = symbol

            df.to_csv(cur+'-'+coin + '0613.csv')

            print(df)
      else:
            print('none')



