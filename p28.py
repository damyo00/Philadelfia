list=list()


def media(list):
    s = 0
    for n in list:
        s += n['voto']
    media = s/len(list)
    return media

allievo=dict()
allievo['nome']='Andrea'
allievo['cognome']='Sansa'
allievo['età']='46'
allievo['test']=[{'voto':20,'data':"1/12/22"},{'voto':30,'data':"3/4/22"},
                 {'voto':25,'data':"3/7/22"},{'voto':35,'data':"4/3/22"}]
list.append(allievo)

allievo=dict()
allievo['nome']='Marco'
allievo['cognome']='Fulfaro'
allievo['età']='30'
allievo['test']=[{'voto':22,'data':"1/12/22"},{'voto':32,'data':"3/4/22"},
                 {'voto':25,'data':"3/7/22"},{'voto':37,'data':"4/3/22"}]      
list.append(allievo)

lista=list()
for n in range(3):
    allievo=dict()
    allievo['nome']=input("nome")
    allievo['cognome']=input("cognome")
    allievo['età']=int(input("età"))
    for x in range(3):
        d=dict()
        lista.append(allievo)

for x in list:
    print(x['nome'],media(x['test']))  
    print(x)