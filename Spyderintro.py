# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 11:23:48 2020

@author: Rachna
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

new= pd.read_csv('AAPL Historical Data.csv',usecols=[0,1,2,3,4])

pohl_avg=new[['Price','Open','High','Low']].mean(axis=1)

obs=np.arange(1,len(new)+1,1
             
plt.plot(obs,pohl_avg,'b',label='My first spyder plot')              
