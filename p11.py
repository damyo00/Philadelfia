from random import randint
k = 0
a = 1
b = 0
while a != b:
    a = randint(1,6)
    b = randint(1,6)
    k = k + 1
    
    print(a,b)
print("Doppio numero in n°",k)