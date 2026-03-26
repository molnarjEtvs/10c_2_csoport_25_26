import os
os.system("cls")

def orszagRogzites():
    orszagokNevei=[]
    while True:
        orszagNev = input("Adja meg az ország nevét:")
        orszagNev = orszagNev.capitalize()
        if not orszagNev:
            break
        else:
            orszagokNevei.append(orszagNev)
    return orszagokNevei

def orszagStatisztika(orszagok:list):
    db = len(orszagok)
    print(f"{db} db ország lett rögzítve")
    darabszam = 0
    for elem in orszagok:
        if elem.find("s")>=0 and elem.find("l")>=0:
            darabszam+=1
        print(f"s és l betűből {darabszam}db van")
    szoveg = orszagok.join("-")
    print(f"Rögzített országok: {szoveg}")
rogzites = orszagRogzites()
orszagStatisztika(rogzites)