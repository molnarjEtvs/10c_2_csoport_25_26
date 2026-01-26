import os,random
os.system("cls")

versenyzok = []
while True:
    nev = input("Add meg a versenyző nevét: ")
    if nev.lower() == "kész":
        break
    rajtszam = int(input("Add meg a rajtszámot: "))
    sebesseg = random.uniform(8,18)
    versenyzo = {}
    versenyzo['nev'] = nev
    versenyzo['rajtszam'] = rajtszam
    versenyzo['sebesseg'] = sebesseg
    versenyzok.append(versenyzo)