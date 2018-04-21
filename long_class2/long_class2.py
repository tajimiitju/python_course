
# coding: utf-8

# In[1]:


#input
height = input('How tall are you? ')

print('How old are you?')
age = input()
print('How old are you?', end=' ')
age = input()


# In[2]:


print(type(age))


# In[3]:


type(age)


# In[1]:


print('How old are you?')
age = int(input())


# In[2]:


type(age)


# In[14]:


#format condition
number = int(input('Enter a number: '))

print(f'{number} is Even? {(number%2)==0}.')


# In[19]:


#format condition
number = int(input('Enter a number: '))

ff = ((number%2)==0)
formattedString = "{} is Even? {}."
print(formattedString.format(number,ff))


# In[21]:


number = int(input('Enter a number: '))

if ((number%2)==0):
    print('Even')
else:
     print('Odd')   


# In[4]:


ps = input('Enter password: ')

if (len(ps)>=6 and len(ps)<=8):
    print('good length')
elif (len(ps)>8):
    print('too long')
else:
    print('too short')


# In[5]:


#advanced printing
print('.' * 10)


# In[6]:


#advanced printing
print('#' * 5)


# In[7]:


# konop jagay cursor rekhe shift+tab dile sob abouyt chgole asbe
#working with Files
#bad practise
f = open("a.txt", 'r') #return a file object , for read = r. for write = w. for read+write = r+
text = f.read()
f.close()
print(text)


# In[8]:


#good practise ... with function e close korte hoyna
with open("a.txt", 'r') as f:
    text = f.read()
print(text)


# In[11]:


try :
    with open("ww.txt", 'r') as f:
        text = f.read()
except FileNotFoundError:
    text = "File Not Found !"
print(text)


# In[12]:


try :
    with open("ww.txt", 'r') as f:
        text = f.read()
except : 
    text = "Error to file open !"
print(text)


# In[13]:


with open('Zila.txt','w') as f:
    f.write('Dhaka')
    f.write('Tangail')


# In[14]:


with open('Zila2.txt','w') as f:
    f.write('Dhaka\n')
    f.write('Tangail')


# In[15]:


with open('Zila3.txt','w') as f:
    print('Dhaka', file = f)
    print('Tangail', file = f)


# In[24]:


c=input('Enter a letter')
if (len(c)==1):
    if (c=='a' or c=='e' or c=='i' or c=='o' or c=='u' or c=='A' or c=='E' or c=='I' or c=='O' or c=='U'):
        print('Vowel')
    else:
        print('Consonant')
else:
    print('invalid input')


# In[30]:


c=input('Enter a letter').lower()
if (len(c)==1):
    if (c=='a' or c=='e' or c=='i' or c=='o' or c=='u'):
        print('Vowel')
    else:
        print('Consonant')
else:
    print('invalid input')


# In[ ]:


c=input('Enter a letter').lower()
if (len(c)==1):
    try:
        cc=int(c)
        print('this is a number')
    except:
        if (c=='a' or c=='e' or c=='i' or c=='o' or c=='u'):
            print('Vowel')
        else:
            print('Consonant')
else:
    print('invalid input')

