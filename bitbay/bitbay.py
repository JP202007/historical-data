import requests
import pandas as pd
pd.set_option('expand_frame_repr', False)


coins={'CTSI','WRX','TROY','KAVA','BAND','PERL','WIN','ERD','ONE','MATIC','CELR','FET','BTT'
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
curs={"USDT-","ETH-","BTC-","EUR-"}

for cur in curs:
    for coin in coins:
        symbol = cur+coin
        url = 'https://api.bitbay.net/rest/trading/candle/history/'+symbol+'/86400?from=1548892800000&to=1589328000000'
        print(url)
        resp = requests.get(url)
        resp_json = resp.json()
        items = resp_json['items']
        df = pd.DataFrame(items)

        if len(df) >0:

            df['market_name'] = symbol
            df.to_csv(symbol + '.csv')
            print(df)
        else:
            print('none')
