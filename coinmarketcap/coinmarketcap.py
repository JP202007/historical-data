import requests
import re
import time
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup as soup

NAME=['cartesi','wazirx','troy','kava','band-protocol','perlin','wink-tronbet','elrond','harmony','matic-network','celer-network',
      'mytvchain','bluekey','synchrobitcoin','wolfs-group','bitcoin-classic','ixinium','meettoken','bitkam','acash-coin',
      'global-crypto-alliance','uos-network','hinto','global-funeral-care','pdata','cryptoads-marketplace','iotw','vindax-coin',
      'stellar-gold','the-hustle-app','redfox-labs','izichain','cryptobuyer','blockium','global-crypto-alliance']

for name in NAME:
    url = 'https://coinmarketcap.com/currencies/' + name + '/historical-data/?start=20190101&end=20200730'
    #pls pay attention on the start time
    headers = {
        'User-Agent': 'Mozilla / 5.0(Macintosh;Intel Mac OS X10_15_4) AppleWebKit '
                      '/ 537.36(KHTML, like Gecko) Chrome / 81.0.4044.138 Safari / 537.36',
        'X-Requested-With': 'XMLHttpRequest'}

    response = requests.get(url, headers=headers)
    response.encoding = response.apparent_encoding
    print(url)
    p_soup = soup(response.text, "html.parser")

    if p_soup.find('div', {'class': 'owj4iq-0 qQkOx'}):
        print('Sorry, we could not find your page')
    elif p_soup.find('div', {'class': 'cmc-table cmc-table--empty sc-1yv6u5n-0 jONMPu'}):
        print('no data to display')
    elif p_soup.find('div', {'class': 'cmc-tab-charts o318p2-0 AyKde'}):
        print('token not exist')
    elif len(p_soup.find('div', {'class': 'cmc-details-panel-price jta9t4-0 fcilTk'}))==2:
        print('This project is featured as an Untracked Listing')
    else:
        html = response.text
        reg1 = re.compile(r'"quotes"([\s\S]*?),"related":')
        data = reg1.findall(html)
        data = data[0]
        reg2 = re.compile(r'"time_open":"([\s\S]*?)T00:00:00.000Z')
        day = reg2.findall(data)
        reg3 = re.compile(r'"close":([\s\S]*?),"volume"')
        close = reg3.findall(data)
        close = np.array(close, dtype='float32')
        reg4 = re.compile(r'"volume":([\s\S]*?),"market_cap"')
        volume = reg4.findall(data)

        day = day[0:]
        close = close[0:]
        volume = volume[0:]

        df = pd.DataFrame({"asset": name, "day": day, "close": close, "volume": volume})
        print(name)
        df.to_csv(name + ".csv", header=True, index=False)
    time.sleep(10)
    #pls set time sleep, cmc set limitation for scrapers, the more data, the longer time sleep
