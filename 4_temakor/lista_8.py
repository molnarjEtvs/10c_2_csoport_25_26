import os
os.system("cls")


szamok = []

for sorszam in range(1,9):
    szam = int(input(f"Add meg a 8/{sorszam} számot: "))
    szamok.append(szam)

kilencek = szamok.count(9)
print(f"9-esek száma: {kilencek} db")