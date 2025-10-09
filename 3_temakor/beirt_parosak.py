import os
os.system("cls")

parosDb = 0
while True:
    szam = int(input("Adj meg egy számot: "))
    if szam<0:
        break
    if szam%2 == 0:
        parosDb +=1

print(f"A párosak száma: {parosDb}")