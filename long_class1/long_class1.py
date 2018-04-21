
# coding: utf-8

# ### Devskill Python Long course class 1 - 20-4-18

# In[6]:


# comment
# koek line eksathe select kore cntrl+/ die multi line cmnt hoy

'''
etake function doc bole bt
eta dieo multi line cmnt kora jay
'''

print('Hello World!')


# In[3]:


print('Hello # World!')


# In[7]:


v1, v2 = 'jayanta','sarker'
a,b,c = 1,True,"jayanta"


# In[8]:


a,b = 4,6


# In[10]:


c=a+b
print('Sum is =',c)


# In[16]:


d='my name is'
e=' tajim'
print(d+e)


# In[17]:


#koma dile auto koma ney
print(d,e)


# In[18]:


a,b=1,1.5
print(type(a))
print(type(b))


# In[19]:


type([1,2,3,4])


# In[20]:


type({1,2,3,4})


# In[21]:


c=(2+5.1j)
print(type(c))


# In[22]:


print(c.real)


# In[23]:


print(c.imag)


# In[27]:


5**3 # 5^3 = 5*5*5 , exponential


# In[28]:


5>5


# In[29]:


5>=5


# In[31]:



# Int to Float

b = 2
print(b)

b = float(2)
print(b)

# Float to complex
c = complex(25.9)
print(c)


print('What is 3 + 2?', 3 + 2)
print('What is 5 - 7?', 5 - 7)

print('What is 3 * 2?', 3 * 2)
print('What is 5 / 7?', 5 / 7)  # Division will always be resulted in float.
print('What is 7 % 2?', 7 % 2)

print('Is it greater?', 5 > -2)
print('Is it less?', 5 < -2)
print('Is it greater or equal?', 5 >= -2)
print('Is it less or equal?', 5 <= -2)


# In[32]:


a=8
b=3
a>b


# In[33]:


c=33
d=44


# In[34]:


(a%b)>(d%c)


# In[36]:


d%c


# In[37]:


a%b


# In[43]:


#Print
my_name = 'Tajim'
my_age = 24
my_weight = 59
my_height = 1.6764

print(f'My name is {my_name}.')
print(f'My name is {my_name} and i am {my_age} years old.')
print(f'My BMI + {my_weight / my_height**2}.')


# In[46]:


funnyOrNot = False
formattedString = "Is that joke funny ? {}"
print(formattedString)


# In[47]:


funnyOrNot = False
formattedString = "Is that joke funny ? {}"
print(formattedString.format(funnyOrNot))


# In[50]:


print('We come here to learn {} {}. and its realy fantastic or not ? {}'.format('python', 3, True))


# In[51]:


print('We come here to learn {} {}. and its realy fantastic or not ? {}'.format('python', 3, funnyOrNot))


# In[52]:


formatter = '{} {} {} {}'

print(formatter.format(1, 2, 3, 4))
print(formatter.format('one', 'two', 'three', 'four'))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))


# In[59]:


m=21
p=4
print('Every person will get {} pcs. The rest will be {}.'.format(m/4,m%4))


# In[60]:


print('Every person will get {} pcs. The rest will be {}.'.format(int(m/4),m%4))


# In[61]:


print('Every person will get {} pcs.\nThe rest will be {}.'.format(int(m/4),m%4))

