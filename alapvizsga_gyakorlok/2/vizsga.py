import os
os.system("cls")

def VizsgaErtekeles(pontSzam:int):
    if pontSzam >= 48:
        return True
    else:
        return False
    
while True:
    nev = input("Adja meg a nevet:")
    pontszam = int(input("Adja meg a pontszamat:"))
    if nev == "":
        break
    else:
        valasz = VizsgaErtekeles(pontszam)
        if valasz == True:
            print(f"{nev} vizsgaja sikeres.")
        else:
            print(f"{nev} vizsgaja sikeretlen.")