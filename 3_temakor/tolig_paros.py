import os
os.system("cls")

tol = int(input("Add meg a kezdő számot"))
meddig = int(input("Add meg a vég számot"))

for szam in range(tol,meddig+1):
    if szam%2==0:
        print(szam)