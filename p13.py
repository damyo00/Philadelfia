from random import randint

sum = 0
for x in range(10):
    a = randint(1,6)
    sum = sum + a
    print(a)
print(sum)