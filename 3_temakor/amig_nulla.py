import os
os.system("cls")

#1 megoldás
szam = 1
osszeg = 0
while szam != 0:
    szam = int(input("Adj meg egy számot: "))
    osszeg += szam
print(f"Összeg: {osszeg}")

#2 megoldás
osszeg = 0
while True:
    szam = int(input("Adj meg egy számot: "))
    if szam == 0:
        break
    osszeg += szam
print(f"Összeg: {osszeg}")