"""
script to review all the NSE listed equities for 2018
"""

import pandas as pd
import numpy as np
import fix_yahoo_finance as datareader


#TODO:
# 1. Analyse daily returns of all stocks
# 2. Compare against market cap of all companies
# 3. Categorize based on sectors/ market cap/ daily volume traded etc


sec_nse = "/Users/ankitgupta/Data/NSE_EQUITY_2018.csv"
sec_bse = ""


startdate = "2018-01-01"
enddate = "2018-12-31"

data_nse = pd.read_csv(sec_nse)
tickers = data_nse["TICKER"].tolist()

data_secs_nse = {}
for ticker in tickers:
    try:
        data_secs_nse[ticker]
    except:
        data_secs_nse[ticker] = pd.DataFrame()

    #get daily prices
    data_secs_nse[ticker]["Price"] = datareader.download(ticker, startdate, enddate)

    #generate daily return
    data_secs_nse[ticker]["Return"] = data_secs_nse[ticker]["Price"].diff()




    


