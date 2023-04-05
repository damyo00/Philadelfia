#riempire una lista e darne la somma in output
from random import randint
l = []
for x in range(10):
    a = randint(1,8)
    l.append(a)
s = 0
for j in l:
    s = s + j
    s += 1
    

print(l)
print(s)  

    