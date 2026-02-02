import os
os.system("cls")

allatok = []
with open("allatok.txt","r",encoding="utf-8") as f:
    for sor in f:
        adatok = sor.strip().split(";")
        allat = {}
        allat['nev'] = adatok[0]
        allat['faj'] = adatok[1]
        allat['suly'] = float(adatok[2])
        allat['kor'] = int(adatok[3])
        allatok.append(allat)

db = len(allatok)
print(f"Állatok száma: {db} db")

oroszlan_db = 0
for allat in allatok:
    if allat['faj'] == "Oroszlán":
        oroszlan_db += 1

print(f"Oroszlánok száma: {oroszlan_db} db")

legnehezebb = allatok[0]
for allat in allatok:
    if allat['suly'] > legnehezebb['suly']:
        legnehezebb = allat

print(f"A legnehezebb állat: {legnehezebb['nev']}, {legnehezebb['suly']}kg")

with open("nyugdijasok.txt","w",encoding="utf-8") as c:
    for allat in allatok:
        if allat['kor']>15:
            c.write(f"{allat['nev']};{allat['faj']}\n")
