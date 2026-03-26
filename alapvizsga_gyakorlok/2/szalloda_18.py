import os, random
os.system("cls")

class Szallashely:

    def __init__(self, szallasNev:str, ar:float, szabadHelyek:int):
        self.szallasNev = szallasNev
        self.ar = ar
        self.szabadHelyek = szabadHelyek

    def helyFrissites(self, db:int):
        self.szabadHelyek += db
        if self.szabadHelyek > 21:
            self.szabadHelyek = 21

    def kedvezmenyGeneralas(self):
        lista = [5,10,20,30]
        self.szazalek = random.choice(lista)
        self.kedvezmenyesAr = self.ar*((100-self.szazalek)/100)
        self.kedvezmenyesAr = round(self.kedvezmenyesAr, 3)

szallasok = []
with open("szallasok.txt", "r", encoding="utf-8") as f:
    for sor in f:
        adatok= sor.strip().split("|")
        szallas1 = Szallashely(adatok[0],float(adatok[1]),int(adatok[2]))
        szallas1.helyFrissites(random.randint(1,21))
        szallas1.kedvezmenyGeneralas()
        szallasok.append(szallas1)
        del szallas1

with open("akciosszallasok.txt","w",encoding="utf-8") as w:
    for szallas in szallasok:
        w.write(f"Szállás neve: {szallas.szallasNev}\n")
        w.write(f"Ár/éjszaka/fő: {szallas.ar} Ft\n")
        w.write(f"Kedvezmény értéke: {szallas.szazalek}%\n")
        w.write(f"Kedvezményes éjszaka ára: {szallas.kedvezmenyesAr} Ft\n")
        w.write(f"Szabad helyek száma: {szallas.szabadHelyek} db\n")
        w.write("#"*30)
        w.write("\n")