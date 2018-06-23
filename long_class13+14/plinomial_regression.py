# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 13:37:16 2018

@author: Tajim
"""


#importing module
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

###load data set
Dataset = pd.read_csv('Position_Salaries.csv')
x=Dataset.iloc[:,1:-1].values
y=Dataset.iloc[:,-1:].values

# x r y diei train korabo, kono test banabona

### start linear regression (univariant)
from sklearn.linear_model import LinearRegression
Regressor = LinearRegression()
Regressor.fit(x, y)

%matplotlib auto

#ploting train data
plt.xlabel("Lavel")
plt.ylabel("Salary")
plt.title("Salary vs Experience (Train Data)")
plt.scatter(x,y,color='blue',marker="x")
plt.plot(x,Regressor.predict(x),color='red') #ekhane regression korle valo line asbena. onk difference thakbe
plt.show()

y_pred=Regressor.predict(np.array([[6.5]]))

'''
Univarient Polynomial
'''

### start linear regression (univariant) polinomial
from sklearn.preprocessing import PolynomialFeatures
poly_regressor = PolynomialFeatures(degree=2) #degree joto besi dibo toto kasakasi line jabe

poly_x = poly_regressor.fit_transform(x)

Regressor_len = LinearRegression()
Regressor_len.fit(poly_x,y)


%matplotlib auto

plt.xlabel("Lavel")
plt.ylabel("Salary")
plt.title("Salary vs Experience (Polynomial Regression)")
plt.scatter(x,y,color='blue',marker="x")
plt.plot(x,Regressor_len.predict(poly_x),color='red') 
plt.show()

