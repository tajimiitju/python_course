# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 17:27:27 2018
day13+14
@author: Tajim
"""

"""
#data pre processing
"""

#importing module
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

###load data set
Dataset = pd.read_csv('Salary_Data.csv')
x=Dataset.iloc[:,:-1].values
y=Dataset.iloc[:,-1:].values

###missing value checking
#Dataset.isnull() #sob gula isnull kina check korbe
Dataset.isnull().values.any() #kono null ase kina ckeck korbe

###no categorical value is here

###no problem in inputs big data value

###data splitting
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,train_size = .8, random_state = 0)

"""
day 14 linear regression
"""
### start linear regression (univariant)
from sklearn.linear_model import LinearRegression
Regressor = LinearRegression()
Regressor.fit(x_train, y_train)
y_pred=Regressor.predict(x_test)

%matplotlib auto

#ploting train data
plt.xlabel("Years Experience")
plt.ylabel("Salary")
plt.title("Salary vs Experience (Train Data)")
plt.scatter(x_train,y_train,color='blue',marker="x")
plt.plot(x_train,Regressor.predict(x_train),color='red') 
plt.show()

#ploting test data
plt.xlabel("Years Experience")
plt.ylabel("Salary")
plt.title("Salary vs Experience (Test Data)")
plt.scatter(x_test,y_test,color='green',marker="o")
#plt.plot(x_train,Regressor.predict(x_train),color='red') 
plt.show()

## HW = see this from net

