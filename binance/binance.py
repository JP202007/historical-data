import requests
import time
import pandas as pd
pd.set_option('expand_frame_repr', False)


limit = 500
end_time = int(time.time() // 60 * 60 * 1000)
start_time = '1546355608000'


curs={'CTSI','WRX','TROY','KAVA','BAND','PERL','WIN','ERD','ONE','MATIC','CELR'}
coins={"USDT","ETH","BTC","BNB"}

for cur in curs:
    for coin in coins:
        symbol = cur+coin
        url = 'https://api.binance.com/api/v3/klines' + '?symbol='+symbol+'&interval=1d&limit=500'+ \
              '&startTime=1546355608000' +'&endTime=' + str(end_time)
        print(url)
        resp = requests.get(url)
        data = resp.json()

        df = pd.DataFrame(data, columns={'open_time': 0, 'open': 1, 'high': 2, 'low': 3, 'close': 4, 'volume': 5,
                                     'close_time': 6, 'quote_volume': 7, 'trades': 8, 'taker_base_volue': 9,
                                     'taker_quote_volume': 10, 'ignore': 11})

        if len(df) > 0:
           df['market_name']=symbol
           df.to_csv(symbol + '.csv')
           print(df)
        else:
          print('none')


