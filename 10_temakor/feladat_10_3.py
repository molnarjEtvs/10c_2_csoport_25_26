import os
os.system("cls")

class Hallgato:

    def __init__(self,azonosito:str,evfolyam:int,kreditszam:int):
        self.azonosito = azonosito
        self.evfolyam = evfolyam
        self.kreditszam = kreditszam

    def targyFelvetel(self,kreditErtek:int):
        self.kreditszam += kreditErtek

    def vizsgazik(self):
        if self.kreditszam>0:
            self.evfolyam += 1
            self.kreditszam = 0
            return True
        else:
            return False
        
    
hallgato1 = Hallgato("abc",9,100)
hallgato2 = Hallgato("xyz",11,45)

hallgato1.targyFelvetel(10) 

if hallgato1.vizsgazik() == True:
    print("hallgató 1 vizsgázott")
else:
    print("hallgató 1 NEM vizsgázott le")

if hallgato2.vizsgazik() == True:
    print("hallgató 2 vizsgázott")
else:
    print("hallgató 2 NEM vizsgázott le")