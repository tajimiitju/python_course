
# coding: utf-8

# In[ ]:

print("Input lengths of the triangle sides: ")
x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))
file = open("testfile.txt","w") 

#file.write("X=",x,", Y=",y,", Z=",z)

if x+y>z and x+z>y and y+z>x :
    if x == y == z:
        print("Equilateral triangle")
        file.write("Equilateral triangle") 
    elif x != y != z:
        print("Scalene triangle")
        file.write("Scalene triangle")
    else:
        print("Isosceles triangle")
        file.write("Isosceles triangle")
else:
    print("Not a triangle at all")
    file.write("Not a triangle at all")