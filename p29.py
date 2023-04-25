L =[22,28,19,30]

def media(lista):
    s = 0
    for n in L:
        s += n
    media = s/len(L)
    return media

def main():
    ris=media(L)
    print(ris)

main()

