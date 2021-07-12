# -*- coding: utf-8 -*-
#import yfinance in terminal, command promt:
#pip install yfinance

import pandas as pd
import numpy as np
import yfinance as yf
import pandas_datareader as pdr
import datetime as dt 
import matplotlib.pyplot as plt
from collections import namedtuple as _namedtuple

ticker = yf.Ticker("NFLX") # Get Ticker of stock

ticker.info

rate = 1

pe = ticker.info['forwardPE']

if (pe < 20):
  rate = rate + 1
  print("noice")
else:
    rate = rate - 1

eps = ticker.info['trailingEps']

if (eps < 1):
  rate = rate - 1
else:
  rate = rate + 1
  print("noice")

roa = ticker.info['returnOnAssets']

if (roa < 0.15):
  rate = rate - 1
else:
  rate = rate + 1
  print("noice")

roe = ticker.info['returnOnEquity']

if (roe < 0.15):
  rate = rate - 1
else:
  rate = rate + 1
  print("noice")

Rgrowth = ticker.info['revenueGrowth']

if (Rgrowth < 0.08):
  rate = rate - 1
else:
  rate = rate + 1
  print("noice")

Rgrowth

quick = ticker.info['quickRatio']

if (quick < 1):
  rate = rate - 1
else:
  rate = rate + 1
  print("noice")

quick

#pm = ticker.info['profitMargins']:

#if (pm < 0.1):
  #rate = rate - 1
#else:
  #rate = rate + 1

if (rate <=  1):
  print("strong sell")
elif (rate <= 2):
  print("sell")
elif (rate <= 4):
  print("neutral")
elif (rate <= 5):
  print("buy")
elif (rate <= 6):
  print("strong buy")
