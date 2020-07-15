# historical-data

This repository lists python codes of IEO tokens' historical data in some crypto exchanges and coinmarketcap. Each folder represents one exchange. You can find both scraping code and merging code. The scraping code refers to the official API document on exchange except coinmarketcap, which can help us to get token's cvs file of historical tradings separately. Another point is that each token would be traded by several coins, like USDT, BTC and ETH. But we cannot know which coin at the first day. Therefore, we need to set coin options including USDT, BTC, ETH  and coin issued by exchange(as BNB for Binance, VD for Vindax).
After we obtain the historical cvs. files for all tokens, we can apply the merging code to involve all the files into one cvs totally. Generally, data scraped from exchanges would set a sequence automatically and the first row is 0. So if we want to extract the trading infomations (price, volume, time etc) at the fisrt listing day, we merely need to filter all "0" of the sequece in the merging cvs file. If the open time is displayed in 10 or 13 digit timestamp format, we need to transfer it to normal time.  So as the first week, month and quarter data.

