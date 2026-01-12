import os
os.system("cls")

szo = input("Adj meg egy szót: ")
szelesseg = int(input("Adj meg egy szélességet: "))
karakter = input("Add meg a kitöltő karaktert: ")
kozepre = szo.center(szelesseg,karakter)
print(kozepre)