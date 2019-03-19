#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 17:24:06 2018

@author: ankit

Setting up HFT Library 
"""

from setuptools import setup, find_packages

setup(name="FDynamics", 
      version=1.0,
      author="Anks",
      description="Libraries used for Financial review as well as Quant research",
      packages=find_packages(exclude=['Testing']),
      zip_safe=False)
