
# coding: utf-8

# In[1]:


#PYTHON DATA STRUCTURE
#SET:

mySet = set()

dir(mySet)


# In[17]:


print(dir(mySet))


# In[2]:



#add
help(mySet.add)


# In[3]:



#add

mySet.add(5)
mySet.add('Five')
mySet.add(True)
mySet.add(5.55)
mySet.add(5 + 5.5j)
len(mySet)


# In[5]:


#set dont maintain order, so ja issa tai dekhabe
mySet


# In[6]:


mySet


# In[7]:


#set dont put duplicate elements, dont save duplicate
set([1,1,1,1,13,3,3,3,3,4,4,4,4,4,4,444,555,555,555,555,6,7,8,8,8,8,9,55])


# In[8]:


print(mySet)
mySet.add(5)
print(mySet)


# In[9]:


#remove discard
help(mySet.remove)
help(mySet.discard)


# In[10]:


mySet.remove('Five')
print(mySet)


# In[11]:



#give error when key can not be removed

mySet.remove('Five')


# In[12]:


mySet.discard(5)
print(mySet)


# In[13]:


#DONT give error when key can not be removed
mySet.discard(5)


# In[14]:


def dis(myst, elem):
    try:
        myst.remove(elem)
    except KeyError:
        pass


# In[15]:


dis(mySet,True)
print(mySet)


# In[16]:


dis(mySet,True)
print(mySet)
dis(mySet,True)
print(mySet)
dis(mySet,True)
print(mySet)
dis(mySet,True)
print(mySet)


# In[18]:


#Faster Way to make set
mySet2 = set([1,2.3,False,'Two'])
len(mySet2)


# In[19]:


mySet2.clear()
len(mySet2)


# In[20]:


#Intergers in 1-10
oddSeries 		= set([1,3,5,7,9])
evenSeries 		= set([2,4,6,8,10])
primeSeries 	= set([2,3,5,7])
compositeSeries = set([4,6,8,9,10])


# In[21]:


oddSeries.union(evenSeries)


# In[22]:


oddSeries.intersection(primeSeries)


# In[23]:


primeSeries.union(compositeSeries)


# In[24]:


print(primeSeries.intersection(compositeSeries))


# In[25]:


primeSeries.intersection(compositeSeries)


# In[26]:


primeSeries.difference(compositeSeries)


# In[27]:


primeSeries.symmetric_difference(compositeSeries)


# In[28]:


6 in oddSeries


# In[29]:


6 in evenSeries


# In[30]:


s1 = set([1,2,3,4,5,6,7,8,9])
s2 = set([1,2,7,9,5])
s1.intersection(s2)


# In[36]:


s1 = {1,2,3,4,5,6,7,8,9}
s2 = {1,2,9,5}
s1.intersection(s2)


# In[50]:


s1 = {1,2,3,4,5,6,7,8,9}
s2 = {1,2,9,5,7}
if(7 in (s1.intersection(s2)) and 6 in (s1.intersection(s2))):
    print(s1.intersection(s2))
    print(s1.union(s2))
elif (6 in s1 and 6 in s2):
    print(s1.union(s2))
elif(7 in s1 and 7 in s2):
    print(s1.intersection(s2)) 
else:
    print(s1.difference(s2))


# In[52]:


if(7 in s1 and 6 in s1 and 7 in s2 and 6 in s2):
    print(s1.intersection(s2))
    print(s1.union(s2))
elif (6 in s1 and 6 in s2):
    print(s1.union(s2))
elif(7 in s1 and 7 in s2):
    print(s1.intersection(s2)) 
else:
    print(s1.difference(s2))


# In[ ]:


#set
# no sort
# no order
# no duplicate
# various type variables
##############################
#list
# can sort
# can order
# can duplicate
# various type variables


# In[53]:


#Lists :
myList = ['aam','jaam','kathal','komola','narikel']
len(myList)
dir(myList)
help(myList.append)
myList.append('lichu')


# In[54]:


myList


# In[55]:


myList[3]


# In[56]:


#0 based index
myList[len(myList)]


# In[57]:


myList[len(myList)-1]


# In[58]:


#direct last index
myList[-1]


# In[59]:


myList[-3]


# In[60]:


#Slicing 
print(myList[2:5]) #5 no er agerta asbe
print(myList[-4:-1]) #-1 er agerta 


# In[61]:


print(myList[2:len(myList)])


# In[62]:


print(myList[2:-1])


# In[66]:


print(myList[-2:6]) #left to right


# In[67]:


myList2 = [1, 2, 3, 4, 5, 1, 2] #A set can store duplicate values.
print( myList2)


#concatintion
print(myList + myList2)


# In[68]:


myList #sudhu laste jog korsilo


# In[69]:


myList.extend(myList2) #value changed


# In[70]:


myList #value changed


# In[72]:


myList2.count(2) #frequency of 2


# In[73]:


myList2.count(1)  #frequency of 1


# In[74]:


print(help(myList2.index))


# In[76]:


myList2.index(2)


# In[84]:


myList2.sort()


# In[85]:


myList2


# In[90]:


myList2.index(2,3,6)


# In[91]:


myList2.index(2,0,6)


# In[92]:


myList2.index(2)


# In[94]:


l1=[1,2,3,5,6,8,8,90]
# loops

mL = [1,2,3,4,5]

for m in mL:
    if m == 3:
        print("found")
#         break
        continue
    print (m)


# In[95]:


for m in mL:
    print (m)


# In[96]:


for m in mL:
    print (m*m)


# In[97]:


for m in mL:
    print (m**2)


# In[98]:


for m in mL:
    print (m**3)


# In[99]:


range(5)


# In[100]:


range(2,5)


# In[101]:


for m in range(5):
    print (m)


# In[102]:


for m in range(1,5):
    print (m)


# In[103]:


print (range(1,5))


# In[104]:


print (list(range(1,5)))


# In[105]:


print (list(range(1,10)))


# In[106]:


print (list(range(1,10,2)))


# In[107]:


for m in range(1,10,2):
    print (m)


# In[109]:


for i in range(1,5,1):
    print (mL[i]**2)


# In[110]:


for i in range(1,5,2):
    print (mL[i]**2)


# In[119]:


mt = ['Amm', 'Jaam', 'Kathal', 'lichu', 'Kola']

for i in range(0,len(mt),2):
    print(i, mt[i], end='\t')


# In[123]:


print (list(range(1,101,1)))


# In[124]:


a=list(range(1,101,1))


# In[125]:


print(a)

