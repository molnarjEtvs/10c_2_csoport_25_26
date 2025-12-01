import os
os.system("cls")

A = int(input("Add meg a km óra állást: "))
B = int(input("Add meg a km óra állást 2: "))
C = float(input("Add meg hány liter benzint tankoltál: "))
benzinAr = int(input("Add meg a benzin liter árát: "))

tavolsag = B-A
atlagFogyasztas = (C/(B-A))*100
koltseg = tavolsag/100*atlagFogyasztas*benzinAr

print(f"Megtett távolság: {tavolsag} km")
print(f"Átlagfogyasztás: {atlagFogyasztas} liter/100km")
print(f"Ez az utad {koltseg} Ft")
