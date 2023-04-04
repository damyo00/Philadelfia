from random import randint
i = 0
while i < 10:
    i = 0
    for x in range(10):
        g = randint(1,100)
        if g > 50:
            i += 1
        print(g)
print(">",i)