import os
os.system("cls")

def utikoltseg_szamitas(tavolsag:int,fogyasztas:float,benzin_ar:float,utasok:int=1):
    uzemanyagfogy = (tavolsag/100)*fogyasztas
    koltseg = uzemanyagfogy*benzin_ar
    koltsegPerFo = koltseg/utasok
    return round(koltsegPerFo)


koltseg1 = utikoltseg_szamitas(500,6,600)
print(f"{koltseg1} Ft")

utasokSzam = int(input("Hány utasod van?: "))

telekocsiKoltseg = utikoltseg_szamitas(200,8,610,utasokSzam)
print(f"Telekocsis ár: {telekocsiKoltseg} Ft")