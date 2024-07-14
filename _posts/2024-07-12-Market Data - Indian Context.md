---
layout: quantBook
title: "Where can I find Data for Indian markets?"
date: 2024-07-12
tags: [Finance, markets, Projectquant]
comments: true
categories: [Projectquant]
---

Lot of times, I have faced challenges finding the right source, and free, for personal research on Indian markets. So, I thought, if its free, researchers should not struggle in finding the source data. They should rather focus on doing the research. 

Listing Publicly available sources for data. Ofcourse, there are other paid services such as Bloomberg, Factset which provide a better view of the market (they are paid services, ofcourse)

**Single Stocks (Equities)**

- Meta Data: 
    - Such as Stock Sector, Industry, etc.
    - Available at eah security's page on NSE. Example: [https://www.nseindia.com/api/quote-equity?symbol=RELIANCE](https://www.nseindia.com/api/quote-equity?symbol=RELIANCE)
    - **Pro**: Dont need regular updates. Once in a quarter is okay.
    - **Con**: No Python API. Write a parser if needed

* Price: 
    - Available at [Yahoo Finance](https://finance.yahoo.com/). 
    - Python API available (yfinance)
    - Historically, better to use BSE as exchange, as Corporate actions are handled better on BSE prices. 2015 onwards, NSE is also good
    - **Pro**: Free, easy to access, with yfinance Python API.
    - **Con**: No support if price issues found. Example: Corporate actions 

* Fundamentals Data: 
    - Available at [Screener.in](https://www.screener.in/)
    - Python API not available. 
    - **Pro**: Free. Good for discretionary investing. 
    - **Con**: 
        - For systematic investing, Data aggregation is a challenge. 
        - Also, not enough history. No direct Python API. Create one if needed. 
        - Screener.in has its own ID for each security. Herculian task to consolidate the list for each security

* Call transripts/ Earnings Announcements
    - _Yet to be figured out_

-----

**NSE Indices**

* Historical Prices:
    - Available at [Nifty Indices](https://www.niftyindices.com/reports/historical-data)
    - Around 80 Indices available, with daily updates
    - **Pro**: Regularly maintained by NSE
    - **Con**: No Python API. Write a parser if needed

* Fundamental Data:
    - Such as Index Dividend Yield, PE Ratio, Price-Book value.
    - Available at [Screener.in](https://www.screener.in/)
    - **Pro**: Free. Good for discretionary investing, and get a sense of overall market 
    - **Con**: 
        - For systematic investing, Data aggregation is a challenge. 
        - Also, not enough history. No direct Python API. Create one if needed. 
        - Screener.in has its own ID for each security. Herculian task to consolidate the list for each security

-----

**India Yield Curve**

* Historical Prices:
    - Available at [Investing.com](https://in.investing.com/rates-bonds/india-5-year-bond-yield-historical-data)
    - **Pro**: Its just the price data, good enough to be used
    - **Con**: 
        - There is a Python API: investpy. But seems like, its not maintained. Facing issues with it regularly. However, investing.com has stopped allowing scraping. So, investpy is of no use.
        - Hard to have a systematic way to get the data on a regular basis

-----

**Economic Indicators Data**

* Historical Data:
    - [moneycontrol.com](https://www.moneycontrol.com/economic-calendar) is a fantastic source for the Indian market economic data
    - **Pro**: Its just data, available on web. Good for discretionary investing.
    - **Con**: Need to systematically parse data frequently to create models looking at economic data

-----

**Market Activity Data**

* Historical Data:
    - Data such as FDI/ FII daily activity: [https://www.fpi.nsdl.co.in/web/Reports/ReportsListing.aspx](https://www.fpi.nsdl.co.in/web/Reports/ReportsListing.aspx)
    - Daily advances/ declines (market depth): [https://www.nseindia.com/historical/advances-declines](https://www.nseindia.com/historical/advances-declines)
    - Options Summarized Data. _Yet to be sourced_


-----
-----

List of data which I need but havent been able to find:
- Futures and Options Data, Daily Close

-----
-----

In case, you are comfortable in paying few bucks, then here are few good sources to procure the data
1. **Bloomberg**. Rarely seen individuals using it due to high cost.
2. Similar to Bloomberg, Factset, Reuters are good enough.
3. [OpenBB](https://openbb.co/) Open BB Terminal. Havent tried it yet, so cant comment much on efficacy.
4. For Indian market Fundamental data,  [Prowess, by CMIE](https://prowessiq.cmie.com/). It is used by academic instutions for their research purposes.


