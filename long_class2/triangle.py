
# coding: utf-8

# In[24]:


a = int(input('Enter First Side : '))
b = int(input('Enter Second Side : '))
c = int(input('Enter Third Side : '))
with open('triangle.txt','w') as f:
    if (a+b>c and b+c>a and c+a>b):
        print('This is a triangle and the triangle is ', end = '') # , end = ''  ..eta dile auto new line ta print korbena 
        f.write('This is a triangle and the triangle is ')
        if(a==b and b==c):
            print('Equilateral = somobahu.')
            f.write('Equilateral.')
        elif(a==b or b==c or c==a):
            print(' = somodibahu')
            f.write('Somodibahu.')
        else:
            print(' = bisomobahu')
            f.write('Bisomobahu.')
    else:
        print('not a triangle')
        f.write('not a triangle.')

