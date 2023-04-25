nomi=['Andrea','Riccardo','Stefano','Nicole','Carlos','Marco']
cognomi=['Sansa','Beraldi','Cesaretti','Pezzi','Andreas','Fulfaro']
nominativi=[]
for n in nomi:
    for c in cognomi:
        nominativi.append(n + " " +c)

print(nominativi)        