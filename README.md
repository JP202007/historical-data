# historical-data

This repository lists python codes of tokens' historical data in some crypto exchanges and coinmarketcap. Each folder represents one exchange. You can find the scraping code and merging code. The merging code is helpful to merge all the cvs files into one cvs totaly. Generally, data scraped from exchanges would set a sequence automatically and the first row is 0. So if we want to extract the trading infomations (price, volume, time etc) at the fisrt listing day, we merely need to filter all "0" of the sequece in the merging cvs file. So as the first week, month and quarter data.

