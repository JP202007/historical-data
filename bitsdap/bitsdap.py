import requests
import pandas as pd

pd.set_option('expand_frame_repr', False)

curs={'BQQQ','CIPX'}

coins={"-USDT","-ETH","-BTC"}

for cur in curs:
    for coin in coins:
        market=cur+coin
        url = "https://api.bq.net/v2/charts/"+market+"?startTime=1546297200000&interval=86400"

        print(url)
        resp=requests.get(url)
        resp_json = resp.json()

        if 'errorCode' in resp_json:
            print('none')
        else:
            df = pd.DataFrame(resp_json)
            df['market_name'] = market
            df.to_csv(market + '.csv')
            print(df)

