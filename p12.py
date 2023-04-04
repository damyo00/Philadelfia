from random import randint
k = 0
g = 0
a = 1
b = 0
c = 1
d = 0
while a != b:
    a = randint(1,6)
    b = randint(1,6)
    k = k + 1
    print(a,b)
print("Doppio numero in n°",k)
while c != d:
    c = randint(1,6)
    d = randint(1,6)
    g = g + 1
    print(c,d)
print("Doppio numero in n°",g)

if k < g:
    print("k ha vinto")
else:
    print("g hai vinto")    