#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 11:12:27 2018

@author: ankit
"""

import pandas as pd
import numpy as np
from collections import OrderedDict

from DataHandler import TBTHandler
from Constants import Constants

Symbol          = "TATAMOTORS"
Date            = "20180220"
Server          = "jp38"
FutContract     = Symbol + "18MARFUT"
FutContractID   = 47875
StrategyID      = 119


#pathTBT     = "~/Documents/TBT_Data/DataStream/" + Symbol + "/"
pathTBT         = "/Users/anks/Google Drive/2017/WallSoft Labs/Scripts/ankit-scripts/Datadump/Ranking/"
fileTBT     = Symbol + "_" + Date + "_RawTicks.csv"
TBT         = pd.read_csv(pathTBT + fileTBT, header = None)        #doesnt contain header information

listTBT     = TBT.values.tolist()
Tickstoprocess = ["N","M","X"]

Booklevels ={}
OrderBook = {}

for item in listTBT:
    
    tick = TBTHandler(item)
    
    if tick.msgType in Tickstoprocess:
        
        if tick.contract not in Booklevels.keys():
            Booklevels[tick.contract] = {"BidSide": {}, "AskSide": {}}
        
        
        
        if tick.direction == "B":
            tick.ProcessOrderTick(Booklevels[tick.contract]["BidSide"])
        
        
        elif tick.direction == "S":
            tick.ProcessOrderTick(Booklevels[tick.contract]["AskSide"])
            
    elif tick.msgType == "T":
        tick.ProcessTradeTick(Booklevels[tick.contract])
        
    
    #update the orderbook with timestamp
    if tick.msgType in Constants.MSG_TYPES:
        
        if tick.contract not in OrderBook.keys():
            OrderBook[tick.contract] = OrderedDict()
            OrderBook[tick.contract] = tick.GetTopNLevelOrderBook(OrderBook[tick.contract], Booklevels[tick.contract], 5)
        
        else:
            OrderBook[tick.contract] = tick.GetTopNLevelOrderBook(OrderBook[tick.contract], Booklevels[tick.contract], 5)
            
        
    
        
