import os,random
os.system("cls")

termekek = []
while True:
    nev = input("Add meg a termék nevét: ")
    if nev.lower() == "vége":
        break
    ar = int(input("Add meg a termék árát: "))
    kedvezmeny = random.uniform(1,30)
    termek = {}
    termek['nev'] = nev #alma
    termek['ar'] = ar #100
    termek['kedvezmeny'] = kedvezmeny #1-30
    termekek.append(termek)

print(termekek)
#írd ki a termék nevét és a kedvezményes árat felsorolva:
for termek in termekek:
    kedvezmenyesAr = termek['ar'] * ((100-termek['kedvezmeny'])/100)
    print(f"{termek['nev']}:{kedvezmenyesAr}")