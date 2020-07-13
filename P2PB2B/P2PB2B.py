import requests
import pandas as pd

pd.set_option('expand_frame_repr', False)

#curs=['VRS','TREEP','KCT','GLDS','TSM','GLDG','STAMP','DXV','BTS','MyTV','QTV','MTMN','L2L','HBXT','BKY','BD','TKS',
     # 'NEXT','SWC','SNB','WLF','BXC','EXMR','XXA','SYN','MTT','COI','RIDE','PIXBY','KAM','TWQ','TRVT','ASTR','GSH',
     # 'NTRT','ESAX','ACA','BOR','CALL','CCC1','UNIS','FLXC','CAND','AX','MoCo','S8','YBY','NCI','CUR8','UOS','HNT',
     # 'CCOH','MBTU','FST','PBET','BWN','GFCS','CMK','UNC','XSCC','LVX','PDATA','GEX','EVED','CRAD','FAIRC',
     # 'XLMG','INX','V4U','YOUR','HELP','ELT','MZG','SET','OSX','ECPN','BELL','TAZ','OXY2','BYGB','SRX','CNTX','BTCWH',
     # 'FUNTO','FLT','PGPAY','HUSL','DBY','GCX'
    #  'IPWT','HINT','RFOX','BBX','IZI','XPT','WPX','REDI','GDEM','PDATA','RES','BOK','BRST','CTT','VRX','XSR','MIKS'
    #  'SWC','BICAS','SWC','ORX','CVA','NF','ORX','CALL','LIB']
curs=['SNB','XXA','MyTV','TSM','QTV','STAMP','VRS','TREEP']
coins={"_USDT","_ETH","_BTC","_USD","_EUR"}
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



