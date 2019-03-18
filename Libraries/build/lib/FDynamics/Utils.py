#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 16:42:34 2018

@author: ankit
"""

import os
import numpy as np
from datetime import datetime

#----------------------------------------------------------------
# Time Handling

def GetReadableTime(TimeStamp):
    #timestamp in epoch (microsecs)
    
    return datetime.fromtimestamp(TimeStamp/1000000).time()


#----------------------------------------------------------------
# File Handling

def CheckFileExists(FileName):

    if os.path.isfile(FileName):
        return True
    else:
        return False


def CheckInvalidPrice(price):
    if np.isnan(price):
        return np.nan
    
    else:
        return price