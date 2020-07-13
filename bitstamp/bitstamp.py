import requests
import pandas as pd
import time
pd.set_option('expand_frame_repr', False)

curs={'ctsi','wrx','troy','kava','band','perl','win','erd','one','matic','celr','fet','btt'
       ,'bxc','cva','bcas','nci','sxc','hnt','gcz','bzo','tcz','nt','fdt','vindax'
        ,'qm','snk','lit','xhd','hdd','benzi','lhd','mcc','upa','iotw','bicoin',
       'vrs','treep','kct','glds','tsm','gldg','stamp','dxv','bts','mytv','qtv','mtmn','hbxt','bky','bd','tks',
      'next','swc','snb','wlf','bxc','exmr','xxa','syn','mtt','coi','ride','pixby','kam','twq','trvt','astr','gsh',
      'ntrt','esax','aca','bor','call','unis','flxc','cand','ax','moco','yby','nci','uos','hnt',
      'ccoh','mbtu','fst','pbet','bwn','gfcs','cmk','unc','xscc','lvx','pdata','gex','eved','crad','fairc',
      'xlmg','inx','your','help','elt','mzg','set','osx','ecpn','bell','taz','bygb','srx','cntx','btcwh',
      'funto','flt','pgpay','husl','dby','gcx'
      'ipwt','hint','rfox','bbx','izi','xpt','wpx','redi','gdem','pdata','res','bok','brst','ctt','vrx','xsr','miks'
      'swc','bicas','swc','orx','cva','nf','orx','call','lib'}
coins={"usd","btc","eur"}


for cur in curs:
    for coin in coins:
        symbol = cur+coin
        url = 'https://www.bitstamp.net/api/v2/ohlc/'+symbol\
              +'/?step=86400&limit=1000'

        print(url)
        resp = requests.get(url)
        text=resp.text

        if text == 'None':
            print('none')

        else:
            resp_json = resp.json()
            data = resp_json['data']
            ohlc = data['ohlc']

            df = pd.DataFrame(ohlc)
            df['market_name'] = symbol
            df.to_csv(symbol + '.csv')
            print(df)


