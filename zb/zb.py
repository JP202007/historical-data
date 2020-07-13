
import requests
import pandas as pd

pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 1000)
#
curs = {'ctsi', 'wrx', 'troy', 'kava', 'band', 'perl', 'win', 'erd', 'one', 'matic', 'celr', 'fet', 'btt'
    , '808ta', 'bxc', 'cva', 'bcas', 'nci', 'sxc', 'hnt', 'gcz', 'bzo', 'tcz', 'nt', 'fdt', 'vindax'
    , 'qm', 'snk', 'lit', 'xhd', 'hdd', 'benzi', 'lhd', 'mcc', 'upa', 'iotw', 'bicoin',
        'vrs', 'treep', 'kct', 'glds', 'tsm', 'gldg', 'stamp', 'dxv', 'bts', 'mytv', 'qtv', 'mtmn', 'l2l', 'hbxt',
        'bky', 'bd', 'tks',
        'next','swc','snb','wlf','bxc','exmr','xxa','syn','mtt','coi','ride','pixby','kam','twq','trvt','astr','gsh',
      'ntrt','esax','aca','bor','call','ccc1','unis','flxc','cand','ax','moco','s8','yby','nci','cur8','uos','hnt',
      'ccoh','mbtu','fst','pbet','bwn','gfcs','cmk','unc','xscc','lvx','pdata','gex','eved','crad','fairc',
      'xlmg','inx','v4u','your','help','elt','mzg','set','osx','ecpn','bell','taz','oxy2','bygb','srx','cntx','btcwh',
      'funto','flt','pgpay','husl','dby','gcx'
      'ipwt','hint','rfox','bbx','izi','xpt','wpx','redi','gdem','pdata','res','bok','brst','ctt','vrx','xsr','miks'
      'swc','bicas','swc','orx','cva','nf','orx','call','lib'}

coins={"_usdt","_eth","_btc","_zb"}

for cur in curs:
  for coin in coins:
      symbol=cur+coin

      url = "http://api.zb.live/data/v1/kline?market="+symbol+"&type=1day"

      print(url)
      resp=requests.get(url)
      data = resp.json()

      df = pd.DataFrame(data, columns={'open_time': 0, 'open': 1, 'high': 2, 'low': 3, 'close': 4, 'volume': 5,
                                       'buy': 6, 'sell': 7})

      if len(df) > 0:
          df['market_name'] = symbol
          df.to_csv(symbol + '.csv')
          print(df)
      else:
          print('none')







url = 'http://api.zb.live/data/v1/kline?market=btc_usdt'
