import os
os.system("cls")

szamok = []
for _ in range(8):
    szoveg = input("Adj meg egy számokat: ")
    if szoveg.isnumeric() == True:
        szamok.append(szoveg)
print(szamok)