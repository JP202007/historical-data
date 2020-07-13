import requests
import pandas as pd
pd.set_option('expand_frame_repr', False)


#curs=['WGRT','NDN','DEP','HDAO','ROAD','XPO','PLG','EC','EM','WXT','ETM','ALV','BLOC']
curs=['WGRT','NDN','DEP']
coins=["-USDT","-ETH","-BTC","-OKB"]

for cur in curs:
    for coin in coins:
        symbol = cur+coin
        #url = 'https://www.okex.com/api/spot/v3/instruments/'+symbol+'/candles?granularity=86400&'+\
         #      '&start=2019-01-01T00:00:00.000Z'+'&end=2019-07-01T00:00:00.000Z'
        #url = 'https://www.okex.com/api/spot/v3/instruments/' + symbol + '/candles?granularity=86400&' + \
         #     '&start=2019-07-01T00:00:00.000Z' + '&end=2020-01-01T00:00:00.000Z'
        url = 'https://www.okex.com/api/spot/v3/instruments/' + symbol + '/candles?granularity=86400&' + \
              '&start=2020-01-01T00:00:00.000Z'
        ##pls notice start time,this API set limitation of 200 max historical data

        print(url)
        resp = requests.get(url)
        data = resp.json()

        df = pd.DataFrame(data, columns={'open_time': 0, 'open': 1, 'high': 2, 'low': 3, 'close': 4, 'volume': 5})

        if len(df) > 0:
           df['market_name']=symbol
           #df.to_csv(symbol+ '1.csv')
           #df.to_csv(symbol+ '2.csv')
           df.to_csv(symbol+ '3.csv')

           print(df)
        else:
          print('none')


