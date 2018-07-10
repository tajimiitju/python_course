# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 10:54:39 2018

@author: DSL-03
"""

# classification = categorical value
# regression = continuous value
# svr = support vector regression
# svm = support vector machine

#importing module
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

### 1. load data set
Dataset = pd.read_csv('Position_Salaries.csv')

### 2. missing value checking
#Dataset.isnull() #sob gula isnull kina check korbe
Dataset.isnull().values.any() #kono null ase kina ckeck korbe

### 3. set x y
x = Dataset.iloc[:,1:-1].values 
y = Dataset.iloc[:,-1:].values


### 8. standard scaller
from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
x = sc_x.fit_transform(x)
sc_y = StandardScaler()
y = sc_y.fit_transform(y)

"""
data preprocessing end
svr start
"""

### svr 1. model selection
from sklearn.svm import SVR
svr_x = SVR(kernel='rbf')
#svr_x = SVR(kernel='linear')
#svr_x = SVR(kernel='poly')
#svr_x = SVR(kernel='sigmoid')
svr_x.fit(x,y)

### svr 2. prediction
y_pred =  svr_x.predict(sc_x.transform(np.array([[6.5]])))
#6.5 number e kirokom asar kotha

### svr 3. reverse transform like first data
y_pred = sc_y.inverse_transform(y_pred)

### svr 4. ploting train data
%matplotlib auto
plt.xlabel("Lavel")
plt.ylabel("Salary")
plt.title("Salary vs Experience (Train Data)")
plt.scatter(x,y,color='blue',marker="x")
plt.plot(x,svr_x.predict(x),color='red') #ekhane regression korle valo line asbena. onk difference thakbe
plt.show()

# python all basic
# web scrapping
# panda + data analysis
# data visualization
# machine learning
