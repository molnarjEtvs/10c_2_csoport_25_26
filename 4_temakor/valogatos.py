import os
os.system("cls")


parosak = []
paratlanok = []

while True:
    szam = int(input("Adj meg egy számot: "))
    if szam == 0:
        break
    if szam%2 == 0:
        parosak.append(szam)
    else:
        paratlanok.append(szam)

print(f"Páros számok\n {parosak}")

print(f"Páratlanok \n {paratlanok}")