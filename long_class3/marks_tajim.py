# coding: utf-8

# In[4]:


#Assignment 1 by tajim
# 3. Write a program to input marks of five subjects Physics, Chemistry, Biology, Mathematics and Computer. 
# Calculate TOTAL percentage(Not Each subject) and grade according to following:
# Percentage >= 90% : Grade A
# Percentage >= 80% : Grade B
# Percentage >= 70% : Grade C
# Percentage >= 60% : Grade D
# Percentage >= 40% : Grade E
# Percentage < 40% : Grade F
# Assume Each exam has 100 marks in total.

Physics = int(input("Enter Physics Marks: "))
Chemistry = int(input("Enter Chemistry Marks: "))
Biology = int(input("Enter Biology Marks: "))
Mathematics = int(input("Enter Mathematics Marks: "))
Computer = int(input("Enter Computer Marks: "))

total_marks = Physics + Chemistry + Biology + Mathematics + Computer

Percentage = (total_marks/500)*100

print('You have got ',Percentage,'% marks and got : Grade ',end='')

if(Percentage>=90):
    print('A')
elif(Percentage>=80):
    print('B')
elif(Percentage>=70):
    print('C')
elif(Percentage>=60):
    print('D')
elif(Percentage>=40):
    print('E')
else:
    print('F')

