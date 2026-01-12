import os,random
os.system("cls")

szam = int(input("Adj meg egy számot 10-1000:"))
genszam = random.randint(10,1000)

print(f"generált: {genszam} | bekért: {szam}")
if szam>genszam:
    print("A bekért szám nagyobb")
elif szam<genszam:
    print("A generált szám nagyobb")
else:
    print("egyenlő")