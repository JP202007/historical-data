import requests
import pandas as pd
import time
pd.set_option('expand_frame_repr', False)

curs=['QM','SNK','LIT','XHD','HDD','BENZI','LHD','MCC','UPA','IOTW','BCT']

coins=["_USDT","_ETH","_BTC","_USD","_BMX","_VET","_BHD"]

end_time = int(time.time() // 60 * 60 * 1000)
print(end_time)

for cur in curs:
    for coin in coins:
      symbol=cur+ coin
      url = "https://openapi.bitmart.com/v2/symbols/"+symbol+"/kline?step=1440&from=1554073558000&to="+str(end_time)

      print(url)
      resp=requests.get(url)
      data = resp.json()
      df = pd.DataFrame(data,columns={'timestamp': 0, 'open_price': 1, 'highest_price': 2, 'lowest_price': 3,
                                  'current_price': 4, 'volume': 5,})

      if len(df) > 0:
            #df.set_index('timestamp', inplace=True)
            df['market_name'] = symbol

            df.to_csv(symbol + '0613.csv')
            print(df)
      else:
            print('none')



