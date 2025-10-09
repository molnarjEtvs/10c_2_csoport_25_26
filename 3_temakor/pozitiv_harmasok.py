import os
os.system("cls")

meddig = int(input("Add meg a számot"))

for szam in range(0,meddig+1):
    if szam%4==0:
        print(szam)