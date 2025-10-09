import os
os.system("cls")

szo = input("Add meg a szót: ")
db = int(input("Add meg a darabszámot: "))

for sorszam in range(1,db+1):
    print(f"{sorszam}. {szo}")