# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 15:58:29 2018

@author: DSL-03
"""
#importing libraries
import pandas as pd
import numpy as np
Dataset = pd.read_csv('Data.csv')
#x1 = Dataset.iloc[:,:-1] #iloc die index paoa jay ":" mane row er sob ":-1" mane column laster ta bad
x = Dataset.iloc[:,:-1].values #values array nilam
#y1 = Dataset.iloc[:,:1] # row sob nilam, column sudhu laster akta nilam
y = Dataset.iloc[:,:1].values

# =============================================================================
# single line cmnt/uncmnt  = cntrl+1
# multi line cmnt = cntrl+4
# multi line uncmnt = cntrl+5
# =============================================================================

from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values="NaN",strategy="mean",axis=0) #cntrl+i dile help e sob asbe
#imputer = imputer.fit(x[:,1:3]) #sob row, 2,3 no column
#x[:,1:3] = imputer.transform(x[:,1:3])

x[:,1:3] = imputer.fit_transform(x[:,1:3])
