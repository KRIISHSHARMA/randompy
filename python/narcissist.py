t = int(input("enter number  : "))
y=t
r=0
o=len(str(t))
for i in range(len(str(t))):
    u=t%10
    t=t//10
    r+=u**o
if r==y : 
    print("nar")
else  : 
    print("autistic")