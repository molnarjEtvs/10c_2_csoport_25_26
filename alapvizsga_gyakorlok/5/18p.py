import random
class Okoscserep:
    def __init__(self,nev:str,fenyigeny:str,vizigeny:str,ultetesHonapja:int):
        self.nev = nev
        self.fenyigeny = fenyigeny
        self.vizigeny = vizigeny
        self.ultetesHonapja = ultetesHonapja
        self.talajnedvesseg = 0
        self.tartalySzint = 100
    
    def napfenySzimulacio(self,ido:int):
        self.talajnedvesseg -= ido/2
        if self.talajnedvesseg<0:
            self.talajnedvesseg = 0

    def locsolas(self,mennyiseg:int):
        self.talajnedvesseg += mennyiseg
        self.tartalySzint -= mennyiseg

    def tartalyToltes(self,mennyiseg:int):
        if self.tartalySzint + mennyiseg > 500:
            self.tartalySzint = 500
            return True
        else:
            self.tartalySzint += mennyiseg
            return False

okosCserepek = []

with open("novenyek.txt","r",encoding="utf-8") as f:
    for sor in f:
        adatok = sor.strip().split("|")
        okoscserep1 = Okoscserep(adatok[0],adatok[1],adatok[2],int(adatok[3]))
        okoscserep1.napfenySzimulacio(random.randint(10,60))
        okoscserep1.locsolas(random.randint(0,50))
        okoscserep1.tartalyToltes(50)
        okosCserepek.append(okoscserep1)
        del okoscserep1

with open("cserpek.txt","w",encoding="utf-8") as s:
    for cserep in okosCserepek:
        if cserep.fenyigeny == "magas":
            s.write(f"Növény: {cserep.nev}\n")
            s.write(f"Fényigény/Vízigény: {cserep.fenyigeny}/{cserep.vizigeny}\n")
            s.write(f"Ültetés hónapja: {cserep.ultetesHonapja}. hónap\n")
            s.write(f"Talajnedvesség: {cserep.talajnedvesseg}%\n")
            s.write(f"Tartályszint: {cserep.tartalySzint}ml\n")
            s.write("*"*50)
            s.write("\n")