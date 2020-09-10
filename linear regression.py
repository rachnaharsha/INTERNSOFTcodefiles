# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 11:10:58 2020

@author: Rachna
"""

#IMPORTING THE LIBRARIES
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



#READING THE DATA FROM THE FILE
readfile=pd.read_csv('advertising.csv')
readfile.head()


#TO VISUALIZE DATA
fig , axs = plt.subplots(1,3,sharey=True)
readfile.plot(kind='scatter',x='TV',y='Sales',ax=axs[0],figsize=[14,7])
readfile.plot(kind='scatter',x='Radio',y='Sales',ax=axs[1],figsize=[14,7])
readfile.plot(kind='scatter',x='Newspaper',y='Sales',ax=axs[2],figsize=[14,7])



#CREATING X AND Y FOR LINEAR REGRESSION
feature_cols = ['TV']
X=readfile[feature_cols]
y=readfile.Sales



#IMPORTING LINEAR REGRESSION ALGORITHM
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(X,y)


print(lr.intercept_)
print(lr.coef_)

#a+bx
result=6.97+0.055*50
print(result)


#CREATE A DATAFRAME WITH MIN AND MAX VALUE OF THE TABLE 
X_new=pd.DataFrame({'TV':[readfile.TV.min(), readfile.TV.max()]})
X_new.head()


preds=lr.predict(X_new)
preds


readfile.plot(kind='scatter',x='TV',y='Sales')

plt.plot(X_new,preds,c='r',linewidth=1)


#SUMMARY OF THE MODEL
import statsmodels.formula.api as smf
lm = smf.ols(formula= 'Sales ~ TV',data = readfile).fit() 
#OLS -> ORDINARY LEAST SQUARED
lm.conf_int() #conf_int() means CONFIDENCE INTERVAL


#FINDING THE PROBABLITY VALUES
lm.pvalues


#FINDING THE RSQUARED VALUES
lm.rsquared


#MULTI LINEAR REGRESSION
feature_cols=['TV','Radio','Newspaper']
X= readfile[feature_cols]
y=readfile.Sales

lr=LinearRegression()
lr.fit(X,y)

print(lr.intercept_)
print(lr.coef_)

lm=smf.ols(formula='Sales ~ TV+Radio+Newspaper',data=readfile).fit()
lm.conf_int()
lm.summary()




