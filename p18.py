from random import randint
l = []
for x in range(10):
        l.append(randint(1,100))
#prima estrarre la serie di numeri e poi contare quelli maggiori di 30.
#sono due operazioni successive

cont=0        
for z in l: 
    if z > 30:
          cont += 1      
        

print(l)    
print(cont)