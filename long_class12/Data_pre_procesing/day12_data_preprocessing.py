

# -*- coding: utf-8 -*-
"""
Created on Sat Jun 9 15:58:29 2018

@author: DSL-03
"""
## start course
# Andrew ng - coursera


#importing module
import pandas as pd
import numpy as np

#load data set
Dataset = pd.read_csv('Data.csv')
x = Dataset.iloc[:,:-1].values # sob row , -1 porjonto ba ses column porjonto, 1 ta kom ney tai laster ta asbena
y = Dataset.iloc[:,-1:].values

# iloc is location of index
# loc is location of row

###day 11
#fit and transform
#feature extruction
#missing value

#handling missing values
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values="NaN",strategy="mean",axis=0) #axis = 0 = column wise, axis = 1 = row wise
x[:,1:3] = imputer.fit_transform(x[:,1:3])

###day 12
###handling categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
x[:,0] #x er 1 no column er slice kore ekta array
xlblEncoder = LabelEncoder()
x[:,0] = xlblEncoder.fit_transform(x[:,0])
xOneHot = OneHotEncoder(categorical_features = [0]) # 0 no column ke same korar jonno
x = xOneHot.fit_transform(x).toarray()
# dummy variable and dummy variable trap hoilo
# 3 ta column hobe 3 ta deser jonno dummy variable trap er jonno jokhon apply korbo machine learning tokhon jekono akta column baddibo

ylblEncoder = LabelEncoder()
y[:,0] = ylblEncoder.fit_transform(y[:,0])
# classification problem e output always categorical hopy. so y categorical, so OneHotEncoder lagbena


### Splitting the data
from sklearn.model_selection import train_test_split
# train r test die data k dui vage vag kori jate performance bojha jay
x_train, x_test, y_train, y_test = train_test_split(x,y,train_size = .8, random_state = 0) #cntrl+i dile help asbe
# 80% data train e rakhlam

### Feature Scalling
#jehetu beton onk besi r boyos kom tai betoner dominance bere gese. bt boyos ta onk important so scale kore eder kasakasi dominance korte hobe

from sklearn.preprocessing import StandardScaler 
sc_x = StandardScaler() # StandardScaleris a class, StandardScaler() is an instance
x_train = sc_x.fit_transform(x_train)
#x_train er sob e kaskasi chole asbe
x_test = sc_x.transform(x_test) # sc_x akbar fit kora hoise, x_test e transform kora baki silo

### data preprocessing ses




