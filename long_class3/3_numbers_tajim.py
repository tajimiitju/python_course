# coding: utf-8

#Assignment 1 by TAJIM
#Write a program to find maximum,minimum,mean between three numbers.

a = float(input("Enter first number: "))
b = float(input("Enter first number: "))
c = float(input("Enter first number: "))

if(a>b and a>c):
    print(a,' is the largest number')
elif(c>b and c>a):
    print(c,' is the largest number')
else:
    print(b,' is the largest number')
    
mean = (a+b+c)/3
print('The mean of the 3 number is: ',mean)
    