import requests
import pandas as pd
import time
pd.set_option('expand_frame_repr', False)

curs={'CTSI','WRX','TROY','KAVA','BAND','PERL','WIN','ERD','ONE','MATIC','CELR','FET','BTT'
       ,'808TA','BXC','CVA','BCAS','NCI','SXC','HNT','GCZ','BZO','TCZ','NT','FDT','VinDAX'
        ,'QM','SNK','LIT','XHD','HDD','BENZI','LHD','MCC','UPA','IOTW','Bicoin',
       'VRS','TREEP','KCT','GLDS','TSM','GLDG','STAMP','DXV','BTS','MyTV','QTV','MTMN','L2L','HBXT','BKY','BD','TKS',
      'NEXT','SWC','SNB','WLF','BXC','EXMR','XXA','SYN','MTT','COI','RIDE','PIXBY','KAM','TWQ','TRVT','ASTR','GSH',
      'NTRT','ESAX','ACA','BOR','CALL','CCC1','UNIS','FLXC','CAND','AX','MoCo','S8','YBY','NCI','CUR8','UOS','HNT',
      'CCOH','MBTU','FST','PBET','BWN','GFCS','CMK','UNC','XSCC','LVX','PDATA','GEX','EVED','CRAD','FAIRC',
      'XLMG','INX','V4U','YOUR','HELP','ELT','MZG','SET','OSX','ECPN','BELL','TAZ','OXY2','BYGB','SRX','CNTX','BTCWH',
      'FUNTO','FLT','PGPAY','HUSL','DBY','GCX'
      'IPWT','HINT','RFOX','BBX','IZI','XPT','WPX','REDI','GDEM','PDATA','RES','BOK','BRST','CTT','VRX','XSR','MIKS'
      'SWC','BICAS','SWC','ORX','CVA','NF','ORX','CALL','LIB','BTC'}
coins={"-USDT","-ETH","-BTC"}

for cur in curs:
    for coin in coins:
        symbol = cur+coin
        url = 'https://api.crex24.com/v2/public/ohlcv?instrument='+symbol\
              +'&granularity=1d&limit=1000'

        print(url)
        resp = requests.get(url)
        data = resp.json()

        if len(data) > 1:

            df = pd.DataFrame(data)
            df['market_name'] = symbol
            df.to_csv(symbol + '.csv')
            print(df)
        else:
            print('none')

        time.sleep(1)


