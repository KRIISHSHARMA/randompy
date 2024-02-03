def forloop(n):
    l = []
    for i in range(n):
        l.append(i)
    return l
def listcomp(n):
    li = [i for i in range(n)]
    return li
    

import random
import time
n = 300000000000
forlooptart1 = time.time()
forloop(n)
end1 = time.time()
print(end1-forlooptart1)
forlooptart2 = time.time()
listcomp(n)
end2 = time.time()
print(end2-forlooptart2)
