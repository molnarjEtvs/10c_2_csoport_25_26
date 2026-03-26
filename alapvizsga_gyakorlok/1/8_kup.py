import os, math
os.system("cls")

try:
    sugar = int(input("Add meg a sugarat: "))
    magassag = int(input("Add meg a magasságot: "))
    pi = 3.14
    V = (sugar**2 * pi * magassag) / 3
    a = (math.sqrt(sugar**2+magassag**2))
    A = (sugar**2 * pi + sugar * pi * a)
    print(f"A térfogat: {round(V,2)}")
    print(f"A felszín: {round(A,2)}")
    if A >= 10:
        print("A felszín legalább tíz.")
except:
    print("Hibás adatbevitel")

