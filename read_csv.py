#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 22:10:21 2020

@author: behnood
"""
import os
import pandas as pd
import pandasql as pds

data_path = os.path.expanduser('~/national-history.csv')

df = pd.read_csv(data_path)

df2 = pds.sqldf("""SELECT COUNT(1), states FROM df GROUP BY death""")
