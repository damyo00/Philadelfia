from random import randint
def creaLista():
    L=[]
    for x in range(10):
        L.append(randint(1,90))
    return L


def somma(L):
    s = 0
    for j in L:
        s = s + j
        s += 1
    return s

def maggiori(G):
    i = 0
    for h in G:
        if h > 50:
            i += 1
            print("I maggiori di 50 sono ",h)

def maggiminor(F):
    t = 0
    for k in F:
        if k > 30 and k < 70:
            t += 1
            print("I compresi sono", k) 

def stampaLista(X):
    for n in X:
        print(n,end= " ")

def main():
    M = creaLista() 
    stampaLista(M)  
    somma(M)
    maggiori(M)
    maggiminor(M)

main()     