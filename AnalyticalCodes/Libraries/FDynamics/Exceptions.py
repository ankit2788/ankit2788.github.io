#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 25 10:19:34 2018

@author: ankit
"""

import logging



class TBTException(Exception):
    """
    Base class for all TBT related exceptions
    """
    
    def __init__(self, msg = None):
        pass


class OrderBookException(Exception):
    """
    Base class for all TBT related exceptions
    """
    
    def __init__(self, msg = None):
        pass


class ContractException(Exception):
    """
    Base class for all Contract exceptions
    """
    def __init__(self, msg = None): 
        pass
    


class EventException(Exception):
    """
    Base class for all Event exceptions
    """
    def __init__(self, msg = None):
        pass
    


class StrategyException(Exception):
    """
    Base class for all Strategy related exceptions
    """
    def __init__(self, msg = None):
        pass
    


class OptionException(Exception):
    """
    Base class for all Option related exceptions
    """
    def __init__(self, msg = None):
        pass



class VisualizationException(Exception):
    """
    Base class for all Visualization related exceptions
    """
    def __init__(self, msg = None):
        pass


class FileMissingException(Exception):
    """
    Base class for all Visualization related exceptions
    """
    Logger = logging.getLogger("FileMissingLogger")

    def __init__(self, FileName = None):
        self.Logger.error("File Missing -- {0}".format(FileName))


class FileEmptyException(Exception):
    """
    Base class for all Visualization related exceptions
    """
    Logger = logging.getLogger("FileEmptyLogger")

    def __init__(self, FileName = None):
        self.Logger.error("File Empty -- {0}".format(FileName))
