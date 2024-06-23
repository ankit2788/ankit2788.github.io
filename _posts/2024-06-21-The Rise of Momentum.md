---
layout: quantBook
title: "Momentum in India"
date: 2024-06-21
tags: [Finance, markets, Projectquant]
comments: true
categories: [Projectquant, Finance]
---


[Factor Investing](https://en.wikipedia.org/wiki/Factor_investing) is not a new topic in the Investing world. Investment Managers, for long, have been extremely keen on factor based Investing methods, and have always been in the search of _market beating factors_. It was first introducted by Harry Markowitz in 1950s as part of [Capital Asset Pricing Model (CAPM)](https://en.wikipedia.org/wiki/Capital_asset_pricing_model) under Modern Portfolio Theory. CAPM introduced the Investing world through the benefits of Diversification and the importance of Efficient frontier. Since then CAPM has been the bedrock of Investment Management.

Eugene Fama and Kenneth French further developed upon the CAPM to introduce 2 new factors that would help determine portfolio's returns. They observed that a certain class of stocks tend to perform better than the market as a whole, i.e. (i) **Small Caps** - _size factor_, (ii) stocks with **higher Book to Market Ratio** - _Value factor_. That led to the formulation of [Fama French 3 - factor model](https://en.wikipedia.org/wiki/Fama%E2%80%93French_three-factor_model)

Factor Investing is a very well researched topic, and there are several journals available detailing it wonderfully. However, most of the research pertains to the developed markets such as United States and Global Markets as a whole. The purpose of this series of articles is to go in depth of nuances pertaining to Indian Markets. The first in this seriesis all about **Momentum Investing**


## History of Momentum Investing in India

Although, one of the early papers in Momentum Investing came in early 1990s, its only in mid 2010s that it started gaining traction in India.

- One of the 1st Momentum based benchmark, S&P BSE Momentum Index was launched only in 2015.
- Later, Nifty followed the suit, and launched NIFTY 200 Momentum 30 Index in 2020.
- Since then, several Momentum based investable products have been launched in the form of Funds or Portfolio Managed services (PMSs)

{% include /momentumHTML/mfAUM.html %} 
<br>
In 2021, UTI was the sole fund manager offering Momentum based funds. Today, there are 12 fund managers offering 40+ funds across categories, totally a monthly average Momentum AUM of 7200 Crores. A massive growth in last 4 years, when the AUM was meagre 12 Crores.

A simple baseline Nifty 200 Momentum 30 Index has given a staggering performance over the benchmark Nifty 200 Index. Nifty 200 Momentum 30 Index is a Long only Momentum index investing in top 30 stocks of Nifty 200 based on the respective momentum score. Methodology details are available [here](https://niftyindices.com/Methodology/Method_NIFTY_Equity_Indices.pdf). In this series, I will expand onto the analysis of Momentum effects and develop a framework for systematic Trend following strategies.
{% include /momentumHTML/momentumVsIndex.html %} 
Baseline Momentum Index (_Nifty 200 Momentum 30 Index_) has generated a CAGR of 14% since 2008, whereas the benchmark Index Nifty 200 returned just over 8.5% CAGR in the time frame. 


## Going deep into Momentum Investing

JPMorgan, in its deep research on [Factor Investing](https://www.cmegroup.com/education/files/jpm-momentum-strategies-2015-04-15-1681565.pdf), primarily for Global and US Markets, had developed a systematic framework to assess Systematic strategies. Somewhat inspired, this series builds upon the research from the lens of Indian markets, and its dynamics. Each Investment strategy comes up with a large possibilities with varying design complexities and challenges, not to forget the risks associated. 
- **Portfolio rebalaning frequency**, i.e., how often one should re-assess the assets in the portfolio and shuffle. 
- What are the **momentum indicators** one can employ. How does the performance of a single Momentum Indicator vary with that of a multiple Momentum Indicator based models. What if you add a market dependent factor in addition to Momentum? What if you change the lookback frquency in the indicator? 
- To what extent the **Asset diversification benefits** occur, i.e. is it good to have 50 stocks in a Momentum portfolio Vs 10 stocks? 
- How would you perform **Capital Allocation** among all these assets? Are all stocks worthy of same weight in the portfolio? 
- Does **Risk Management** help?


### Risks Associated

Momentum, as the name suggests, carries the charge. In market bullish times, Nifty 200 Momentum 30 Index, _a long only portfolio,_ tends to out-perform the market. However, during market downturns, the momentum carries, and it fails to beat the market during those times. Table 1 displays the Best and worst 10 months for the Momentum index. This is clearly a case of **incorrectly identifying the trend**.

{% include /momentumHTML/momentumVolatile.html %}

<br>
Figure 3 _(above)_ and Table 1 _(below)_ illustrates the performance of Momentum strategies during volatile periods. Most of the worst months occured during the 2008 market crash. In those months, Momentum **underperformed** the market, due to trend mis-identification. 
<br>

<p class="aligncenter"> 
<img src="/data/pics/momentum/months.png" alt="Best and worst months"  width="980" height="320" text-align="left"/>
</p>

<br>
In addition to downturn volatile periods, **underperformance occurs during periods with No Clear trend**, i.e. a mean reverting (_stationary_) markets. In addition to market specific risks, there could be risks associated with **_not so ideal backtests_**. Indian markets dont have a long performance history, due to the not so matured nature of the markets. The backtests, hence, may suffer from **Survivorship bias**, wherein only those listed securities are chosen in the backtest which are still available for public investing. 



## Base Momentum Fund - The Prototype

### Portfolio Selection

Designing the fund entails, selecting the underlying assets, choice of metrics used to identify Momentum, as well as technical implementations such as rebalancing frequency, transaction costs etc. The selection of assets is done on a relative basis, called **Relative Momentum Strategies**, 


<p align="center"> 
<img src="/data/pics/momentum/relative.png" alt="Relative Momentum Strategy"  width="510" height="320" text-align="center"/>
</p>

<br>
To construct and test Momentum Strategies, we would take _top 10_ stocks from Nifty 50 Index _every month_, with _Equal Weightage_ assigned to them every month. We assume a cost of 14 bps on every transaction, which is inclusive of all transaction cost, brokerage fee and taxes on NSE. We will construct the base prototype with 12 month lookback window for the momentum indicator, i.e. identifying stocks with best returns in the last 12 months, skipping the recent 1 month to avoid the "reversal effects", as shown by _Jegadeesh and Titman (1993)_. The portfolio's performance will be compared with Nifty 50's performance during the time. In addition to 12 month Momentum indicator, I will construct 1-, 3-, and 6- months indicators.

The portfolio will start from 1st Jan 2008, the year of Global Financial meltdown. As seen above, I expect the base prototype not to perform better that year. 


> **NOTE**: There is a survivorship bias, as latest Nifty 50 constituents are used to construct Momentum portfolio in the past.
<br>


### Performance Study

{% include /momentumHTML/CumPerformance_Base.html %}

<br>
<br>

<p align="center"> 
<img src="/data/pics/momentum/basePerformance.png" alt="Base Performances"  width="1000" height="260" text-align="center"/>
</p>
<br>

The performance usually erodes as the time horizons for calculating the trend signals get shorter. On a full Backtesting period from 2008 onwards, the 12-month Momentum signal yielded a CAGR of nearly 16.8% whereas 1-month signal underperformed with CAGR of just over 13%, still better than Nifty50. The numbers drastically change when the model ran from 2010 onwards, i.e. removing the Financial crisis times. 12-month momentum signal generated CAGR of 20.6%, whereas 6-month and 3-month signals merely reached 16% CAGR. On risk adjusted basis, still longer duration momentum signal outperformed others as well as Nifty50.


### Trend Diversification Benefits? 
{% include /momentumHTML/RollingCorr_Base.html %}
<br>


Figure 5 (above) show the running correlation of Momentum Strategies with the benchmark, along with the VIX levels. Since the base prototype strategies only differ in the duration of the trend signal, the correlations are pretty high. Hence, the trend diversification benefits may not be significant.


## Conclusion
In the 1st part of this series, we briefly touched base on the history of Momentum Investing in India, and how this has been the poster boy of Factor Investing in recent times. Besides, we constructed our base Relative Momentum Portfolio with a simple trend following strategy, which did outperform the benchmark. 

The next article will talk about different trend filters, and how a combination of filters can impact the performance of the strategy. Stay tuned!


# Appendix

> 1. Research Details & Source: **Project Quant**, by _Ankit Gupta_
