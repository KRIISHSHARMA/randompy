import math
x1 = float(input("enter x1 : "))
x2 = float(input("enter x2 : "))
y1 = float(input("enter y1 : "))
y2 = float(input("enter y2 : "))

D = math.sqrt((x2-x1)**2 + (y2-y1)**2)
print(D)

# using function
x=[x1,y1]
y=[x2,y2]
print(math.dist(x,y))