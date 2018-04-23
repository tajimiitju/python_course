
# coding: utf-8

# In[ ]:

print("Input lengths of the triangle sides: ")
x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))

if x+y>z and x+z>y and y+z>x :
    if x == y == z:
        print("Equilateral triangle")
    elif x != y != z:
        print("Scalene triangle")
    else:
        print("Isosceles triangle")
else:
    print("Not a triangle at all")

