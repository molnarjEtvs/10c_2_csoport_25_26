import os, random
os.system("cls")

class Macska:
    def __init__(self, nev:str, kor:int, fajta:str):
        self.nev = nev
        self.kor = kor
        self.fajta = fajta
        self.ehseg = 50
        self.mozgasigeny = 0

    def etetes(self, mennyiseg:float):
        self.ehseg -= mennyiseg

        if self.ehseg < 0:
            self.ehseg = 0

    def jatszas(self, ido:int):
        self.mozgasigeny -= ido
        if self.kor < 1:
            self.ehseg += ido * 2
        else:
            self.ehseg += ido

    def alvas(self, ido:int):
        self.mozgasigeny += ido
        if ido >= 8:
            self.ehseg += 5
        else:
            self.ehseg += 2
    
    def setallapot(self):
        if self.ehseg<20:
            self.allapot="ehes"
        elif self.ehseg >=20 and self.ehseg<60:
            self.allapot="ehesen jarkal"
        else:
            self.allapot="Jol lakott"

macskak = []
with open("macskak.txt","r",encoding="utf-8") as f:
    for sor in f:
        adat=sor.strip().split(",")
        macska1 = Macska(adat[0], int(adat[1]), adat[2])
        macska1.jatszas(random.randint(5,10))
        macska1.etetes(random.randint(1,5))
        macska1.alvas(random.randint(5,10))
        macska1.setallapot()