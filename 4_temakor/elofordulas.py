import os
os.system("cls")

szamok = []

while True:
    szam = int(input("adj meg egy egész számot: "))
    if szam == 0:
        break
    if szam>=1 and szam<=5:
        szamok.append(szam)
    else:
        print("A számot nem tudom eltárolni! Lehetésges: 1-5")

egyesek = szamok.count(1)
kettesek = szamok.count(2)
harmasok = szamok.count(3)
negyesek = szamok.count(4)
otosok = szamok.count(5)

print(f"1-es: {egyesek}db\n2-es: {kettesek}db\n3-as: {harmasok}db\n4-es: {negyesek}db\n5-ös: {otosok}db")
