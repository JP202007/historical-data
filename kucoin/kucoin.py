import requests
import pandas as pd
pd.set_option('expand_frame_repr', False)


curs={'LYXe','TOKO','COTI','TRY','MTV','BTC'}
coins={"-USDT","-ETH","-BTC","-KCS"}

for cur in curs:
    for coin in coins:
        symbol = cur+coin
        url = 'https://api.kucoin.com/api/v1/market/candles?type=1day&symbol='+symbol
        print(url)
        resp = requests.get(url)
        resp_json = resp.json()
        code = resp_json['code']

        if code == '200000':
            data = resp_json['data']
            df = pd.DataFrame(data, columns={'time': 0, 'open': 1, 'close': 2, 'high': 3, 'low': 4, 'volume': 5
                , 'turnover': 6})

            df['market_name'] = symbol
            df.to_csv(symbol + '.csv')
            print(df)
        else:
            print('none')
