# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 17:27:27 2018

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
x_tain, x_test, y_train, y_test = train_test_split(x,y,train_size = .8, random_state = 0)

### start linear regression
