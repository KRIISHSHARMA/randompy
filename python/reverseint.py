int1=int(input("enter number to reverse"))
int1 = str(int1)
b= int1[::-1]
for i in b:
    print(i+" ",end=" ")
    
# in answer they used 
f = " ".join(b)
print(f)