# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 4:36 2018
day15
multiple linear regression
@author: Tajim
"""

"""
data pre processing
"""

#importing module
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

### 1. load data set
Dataset = pd.read_csv('50_Startups.csv')

### 2. missing value checking
#Dataset.isnull() #sob gula isnull kina check korbe
Dataset.isnull().values.any() #kono null ase kina ckeck korbe

### 3. set x y
x = Dataset.iloc[:,:-1].values 
y = Dataset.iloc[:,-1:].values

### 4. handling categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
x[:,3] 
xlblEncoder = LabelEncoder()
x[:,3] = xlblEncoder.fit_transform(x[:,3])

### 5. same wait the data
xOneHot = OneHotEncoder(categorical_features = [3]) 
x = xOneHot.fit_transform(x).toarray()

### 6. same wait the data
x = x[:,1:] #first column ta baddilam

### 7. Splitting the data
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,train_size = .8, random_state = 0) 

### 8. standard scaller not need because regeression e nie nibve auto


"""
Linear regression
"""
from sklearn.linear_model import LinearRegression
Regressor = LinearRegression()
Regressor.fit(x_train, y_train)
y_pred=Regressor.predict(x_test)


"""
Multiple linear regression:
Important column finding:
1. All in
2. Backward Elemenation
3. Forward Seletion
4. Bidirectional

Forward Seletion Steps:
        1. select significance level (.05)
        2. predict y with each independent variable (single linear rergession) and get p value
        3. p-value jetar sobche kom seta best. lowest p-value will be taken
        4. jei column ta nilam setar sathe ar akta kore nie 2 ta 2ta kore abr y predict kore p value nibo
        5. tarpor abr p value theke kom ta nibo
        6. jetar p value .05 theke besi asbe seta bad. 
        7. p value onujai jekota nilam tader combination er abr p value nibo. jokhon 0.05 er che besi asbe tokhon bad.


Backward Elemenation Steps:
        1. same
        2. not all -> each
        3. 
        
        
ols = optomal list square b    
"""

### Backward Elemenation
import statsmodels.formula.api as sm

### new first column banano 1 die, y = b1 + b2x er equation banabo, b1 tra bosalam, regression e eta kore nite hoy. onno analysis e lagena
x = np.append(arr = np.ones(shape=(50,1)).astype(int), values = x, axis = 1) 
#astype die type change korlam
# prothome akta column add korlam sob gula 1 er...50 ta 1 die
# axis = 1 dile column add korbe, axis = 0 dile row add korto

x_opt = x[:,[0,1,2,3,4,5]]
regressor_OLS = sm.OLS(endog = y, exog=x_opt).fit()
#endog = dependent, exog = independent
regressor_OLS.summary()

# 2 highest silo tai bad

x_opt = x[:,[0,1,3,4,5]]
regressor_OLS = sm.OLS(endog = y, exog=x_opt).fit()
#endog = dependent, exog = independent
regressor_OLS.summary()

# 1 highest silo tai bad

x_opt = x[:,[0,3,4,5]]
regressor_OLS = sm.OLS(endog = y, exog=x_opt).fit()
#endog = dependent, exog = independent
regressor_OLS.summary()

# x2=4 highest silo tai bad

x_opt = x[:,[0,3,5]]
regressor_OLS = sm.OLS(endog = y, exog=x_opt).fit()
#endog = dependent, exog = independent
regressor_OLS.summary()

# x2=5 highest silo tai bad

x_opt = x[:,[0,3]]
regressor_OLS = sm.OLS(endog = y, exog=x_opt).fit()
#endog = dependent, exog = independent
regressor_OLS.summary()

### num 3 thaklo... so its most important column

# ebar sudhu 3 no die predict korbo
###predict value with optimal feature
regressor_opt = LinearRegression()
regressor_opt.fit(x_train[:,2:3],y_train) #er sudhu oi 3 no ta nilam
y_pred_opt = regressor_opt.predict(x_test[:,2:3])


