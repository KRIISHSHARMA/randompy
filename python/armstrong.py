t = int(input("enter number  : "))
y=t
r=0
for i in range(len(str(t))):
    u=t%10
    t=t//10
    r+=u**3
print(r)
if r==y : 
    print("armstong")
else  : 
    print("autistic")