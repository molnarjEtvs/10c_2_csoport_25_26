import os 
os.system("cls")

try:
    eredetiAr=int(input("Add meg a termék árát: "))
    db = int(input("Termékek száma: "))
    kedvezmeny = float(input("Mekkora a kedvezményed: "))

    kedvezmenyesAr = eredetiAr - (eredetiAr * (kedvezmeny/100))
    kedvezmenyesAr = round(kedvezmenyesAr, 2)
    osszesKedvezmeny = kedvezmenyesAr * db
    eredetiAr2 = eredetiAr * db
    osszKedvezmeny = eredetiAr2 - osszesKedvezmeny
    if osszKedvezmeny > 20000:
        osszKedvezmeny = 20000
    print(f"Egy db termék kedvezményes ára: {kedvezmenyesAr}Ft")
    print(f"A kedvezményes ár összesen: {osszesKedvezmeny}")
    print(f"Az eredeti ár összesen: {eredetiAr2}")
    print(f"Az össze kedvezmény: {osszKedvezmeny}")
except:
    print("Hibás adatbevitel!")
