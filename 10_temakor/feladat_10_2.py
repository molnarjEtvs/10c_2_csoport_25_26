import os
os.system("cls")

class Szamitogep:

    def __init__(self,szabadth:float,allapot:bool,azonosito:str):
        self.szabadth = szabadth
        self.allapot = allapot
        self.azonosito = azonosito
    
    def kapcsol(self):
        if self.allapot == False:
            self.allapot = True
        else:
            self.allapot = False
    
    def programMasol(self,meret:float):
        if meret<=self.szabadth and self.allapot == True:
            self.szabadth -= meret
            return True
        return False
    

gep1 = Szamitogep(2000,False,"abc")
gep2 = Szamitogep(200,False,"123")
gep1.kapcsol()
gep1.programMasol(800)
gep1.programMasol(400)
gep2.programMasol(1)