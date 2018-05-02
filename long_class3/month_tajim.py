# coding: utf-8

# In[4]:


#Assignment 1 by tajim
#2. Write a program to input month number and print number of days in that month.

# Month
# January, March, May, July, August, October, December have	31 days
# February has 28/29 days
# April, June, September, November have 30 days


m = int(input("Enter month number: "))
if(m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12):
    print('It contains 31 days.')
elif(m==2):
    print('It contains 28/29 days.')
else:
    print('It contains 30 days.')