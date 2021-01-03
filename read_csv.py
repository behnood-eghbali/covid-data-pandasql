#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 22:10:21 2020

@author: behnood
"""
import os
import pandas as pd
import pandasql as pds
import matplotlib.pyplot as plt

data_path = os.path.expanduser('~/national-history.csv')

df = pd.read_csv(data_path)

df2 = pds.sqldf(""" SELECT positive FROM df GROUP BY strftime('%m', date) """)

df3 = pds.sqldf(""" SELECT negative FROM df GROUP BY strftime('%m', date) """)

df4 = pds.sqldf(""" SELECT death FROM df GROUP BY strftime('%m', date) """)

plt.figure()

df2.plot.area()
df3.plot.area()
df4.plot.area()
