#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 10:49:53 2019

@author: ankitgupta
"""


import pandas as pd
import numpy as np
import os
from functools import reduce
from datetime import datetime
from FDynamics.Visualizations import CurveAnimation
from matplotlib import animation


class BondYieldCurve(CurveAnimation):
    
    def __init__(self, Maturity, YieldDetails, YieldLabels):
        '''
        Initialize the Animation object with below attributes:
        Inputs: 
            YieldLabels 
            YieldDetails --> tuple of Yield Curves at every instant 
            YieldLabels --> name of the YieldCurves to be plotted
            
        '''

        super().__init__(Maturity, YieldDetails, YieldLabels)


    def initFigure(self, Plotlimits = None , fig = None, axis = None):
        '''
        If plot limits are not provided, this method sets the limits, 
        and then calls the base class method of initailizing the figure
        '''

        #set plot limits
        if Plotlimits is None:
            Plotlimits      = self._getLimits()

        #calling base class method
        fig, axis = super().initFigure(Plotlimits, fig, axis)
        return fig, axis


    def initPlotElements(self, axis = None):
    
        pass


    def initAnimation(self):
        pass

    def SequentialAnimate(self, frame, timer_in_epoch):
        pass

    def RunAnimation(self, Plotlimits = None, fig = None, axis = None, interval = 10):

        timer_in_epoch = False
        time_dateobject = True

        #Create the figure for animation
        figure, axes = self.initFigure(Plotlimits, fig, axis)
        

        #Initialize the Plot element which is supposed to be animated
        super().initPlotElements(axes)
        axes.legend()

        anim = animation.FuncAnimation(figure, 
                                    super().SequentialAnimate, init_func=super().initAnimation, 
                                    frames=len(self.Timers), fargs = (timer_in_epoch, time_dateobject,), interval=interval, 
                                    blit=True, repeat = False)



        return anim

        
    def _getLimits(self):
        '''
        Function to set the limits required for plotting purposes
        '''
        
        
        #get the plot limits        
        temp_Mat = np.ravel(self.X_AxisDetails)
        temp_Yield = np.ravel(self.CurveDetails[0])

        LowYield = np.nanmin(temp_Yield)
        HighYield = np.nanmax(temp_Yield)

        MatLimit            = (0, np.nanmax(temp_Mat)+5)
        YieldLimit           = (LowYield - 1, HighYield + 1)

        return MatLimit, YieldLimit


path = "/Users/ankitgupta/Data/IndiaBondData/"
file = "IndiaBondYields.csv"


def convert(s):
    try:
        return int(s)
    except ValueError:
        return float(s)

#-----------Arrange Data----------


files = []

for filename in os.listdir(path):
    
    if "Bond Yield" in filename:
        #maturity = filename.split("-")[0][6:] + "Y"
        maturity = filename.split("-")[0][6:]
        month_year = filename.split("-")[1][:5]
        if month_year.upper() == "MONTH":
            maturity = str(float(maturity)/12)
        
        yearyield = pd.read_csv(path + filename)
        yearyield[maturity] = yearyield["Price"]
        yearyield["DATE"] = yearyield["Date"].apply(lambda x:datetime.strptime(x, '%b %d, %Y').date() )
        yearyield = yearyield[["DATE", maturity]]
        
        yearyield = pd.DataFrame(yearyield)
    
    
        files.append(yearyield)




df_merged = reduce(lambda  left,right: pd.merge(left,right,on=['DATE'],
                                            how='outer'), files).fillna(np.nan)
df_merged.set_index("DATE", drop=True, inplace=True)
df_merged.sort_index(axis=0, inplace = True)

#sort columns
temp_col = []
cols = list(df_merged.columns)
temp_col = [convert(year) for year in cols]
temp_col.sort()

new_cls = [str(year) for year in temp_col]
#new_cls = temp_col

IndiaBondYields = df_merged[new_cls]
IndiaBondYields.to_csv(path + file)

maturity = [temp_col] * len(list(IndiaBondYields.index))
Maturity = pd.DataFrame(maturity, index = IndiaBondYields.index)



#animation
a = BondYieldCurve(Maturity, (IndiaBondYields, ), ("India Yield Curve",))
a.RunAnimation(interval=70)

