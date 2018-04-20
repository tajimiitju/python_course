#Taking Inputs

a = int(input('please enter 1st arm '))
b = int(input('please enter 2nd arm '))
c = int(input('please enter 2nd arm '))

#Check for tribhuj Definition

if ((a >= b + c) or (b >= a + c) or (c >= a + b)):
    print('This is not a triangle')
else :
    #Opening a File
    with open('tribhuj.txt','w') as f:
        #check for Somobahu
        if a==b and b==c and a==c :
            f.write('Somobahu tribhuj')
        #Check for Bishombahu
        elif a!=b and b!=c and a!=c :
              f.write('Bishombahu tribhuj')
        #Remaining Somodibahu
        else:
             f.write('Somodibahu tribhuj')
     