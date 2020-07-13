import requests
import pandas as pd

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
      'SWC','BICAS','SWC','ORX','CVA','NF','ORX','CALL','LIB'}

coins={"USDT","ETH","BTC","CET","BCH"}

for cur in curs:
    for coin in coins:
        market=cur+coin
        url = "https://api.coinex.com/v1/market/kline?market="+market+"&type=1day&limit=1000"

        print(url)
        resp=requests.get(url)
        resp_json = resp.json()
        df1 = pd.DataFrame(resp_json)

        if len(df1) > 1:
            data = resp_json['data']
            df = pd.DataFrame(data,columns={'time': 0, 'open': 1, 'close': 2, 'highest': 3, 'lowest': 4, 'volume': 5,
                                    'amount': 6, 'market_name': 7})
            df['market_name'] = cur+coin
            df.to_csv(cur+coin + '.csv')
            print(df)

        else:
            print('none')
