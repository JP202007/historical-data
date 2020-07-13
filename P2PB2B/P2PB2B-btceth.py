import requests
import pandas as pd

pd.set_option('expand_frame_repr', False)

curs={'BTC','ETH'}

coins={"_USDT","_USD"}
for cur in curs:
    for coin in coins:
        market=cur+coin
        url = "http://api.p2pb2b.io/api/v2/public/market/kline?"+"market="+market+"&interval=1d&limit=500"

        print(url)
        resp=requests.get(url)
        data = resp.json()
        results=data['result']
        df = pd.DataFrame(results,columns={'open_time': 0, 'open': 1, 'close': 2, 'highest': 3, 'lowest': 4, 'volume': 5,
                                    'amount': 6, 'market_name': 7})

        if len(df) > 0:
            #df.set_index('open_time', inplace=True)
            df['market_name'] = market

            df.to_csv(market + '.csv')
            print(df)
        else:
            print('none')



