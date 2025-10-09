import os
os.system("cls")

szektorAr = 6500
paholyAr = 9800
vegosszeg = 0
kedvezmenySzorzo = 0.75 

tipus = input("Hova szeretnél jegyet? Páholy(P), Szektor(S): ")
db = int(input("Add meg a jegyek számát: "))
diake = input("Diák vagy? igen(i), nem(n): ")

if tipus == "P":
    vegosszeg += paholyAr*db
elif tipus == "S":
    vegosszeg += szektorAr*db

if diake == "i":
    vegosszeg *= kedvezmenySzorzo

print(f"Fizetendő: {vegosszeg} Ft")