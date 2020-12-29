import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
pfizer=yf.Ticker("PFE")
pfizerData=pfizer.history(period='1y')
pfizerData.drop(labels=['Dividends','Stock Splits'],axis=1,inplace=True)
pfizerData.Volume=np.log(pfizerData.Volume)
pfizerData['Variability']=pfizerData.High-pfizerData.Low