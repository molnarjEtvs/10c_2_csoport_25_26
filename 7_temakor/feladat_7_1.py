import os
os.system("cls")

telefonkonyv = []

#adatfeltöltés
while True:
    ember = {}
    ember['nev'] = input("add meg a nevet:")
    if ember['nev'].upper() == "VÉGE":
        break
    else:
        ember['telefonszam'] = input("Add meg a telszámot: ")
        telefonkonyv.append(ember)

#keresés:
nev = input("Keresett név: ")
talalat = ""
for keresettEmber in telefonkonyv:
    if keresettEmber['nev'] == nev:
        talalat = keresettEmber['telefonszam'] 
#kiírás
if talalat == "":
    print("NINCS TALÁLAT")
else:
    print(talalat)