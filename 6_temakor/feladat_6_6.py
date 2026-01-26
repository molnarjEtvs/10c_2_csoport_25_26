import os
os.system("cls")

szavak = []
for _ in range(6):
    szoveg = input("Adj meg egy szöveget: ")
    if szoveg.isalpha() == True:
        szavak.append(szoveg)
print(szavak)