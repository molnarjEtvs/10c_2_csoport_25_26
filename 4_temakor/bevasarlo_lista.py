import os
os.system("cls")

termekek = []
sorszam = 1
while True:
    termek = input(f"Add meg a(z){sorszam}. termék nevét: ")
    if not termek:
        break
    termekek.append(termek)
    os.system("cls")
    sorszam += 1

torlendo = input("Mit szeretnél törlni?: ")
if torlendo in termekek:
    termekek.remove(torlendo)
else:
    print("Nincs ilyen termék")

sorszam = 1
for termek in termekek:
    print(f"{sorszam}. {termek}")
    sorszam += 1