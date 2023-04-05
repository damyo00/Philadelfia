#creo una lista e successivamente conto quanti sono > 30 e < 70.
from random import randint
l = []
i = 0
for x in range(20):
    a = randint(1,100)
    l.append(a)
    l.sort()
"""    
    if a > 30 and a < 70:
        i += 1    
print(l)
print(i)  
"""
cont = 0
for e in l:
    if e > 30 and e < 70:
        cont += 1
print(l)
print(cont)        