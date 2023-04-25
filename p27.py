nomi = ['Andrea','Stefano','Marco','Riccardo','Carlos','Nicole']
d=dict()
d[1]='Andrea'
d[2]='Nicole'
d[3]='Marco'
d[4]='Stefano'
d[5]='Carlos'
d[6]='Riccardo'

anagrafe=[]
giocatore=dict()
giocatore['portiere']="andrea"
anagrafe.append(giocatore)
giocatore=dict()
giocatore['terzino']="riccardo"
anagrafe.append(giocatore)
giocatore=dict()
giocatore['centravanti']="stefano"
anagrafe.append(giocatore)
for x in anagrafe:
    print(x)
