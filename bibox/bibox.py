import requests
import pandas as pd

pd.set_option('expand_frame_repr', False)

curs={'XENO','FOR'}

coins={"_USDT","_ETH","_BTC","_BIX"}

for cur in curs:
    for coin in coins:
        market=cur+coin
        url = "https://api.bibox.com/v1/mdata?cmd=kline&pair="+market+"&period=day"

        print(url)
        resp=requests.get(url)
        resp_json = resp.json()
        df1 = pd.DataFrame(resp_json)

        if len(df1) > 2:
            result = resp_json['result']
            df = pd.DataFrame(result)
            df['market_name'] = market
            df.to_csv(market + '.csv')
            print(df)

        else:
            print('none')
