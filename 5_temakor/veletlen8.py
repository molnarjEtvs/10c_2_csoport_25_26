import os,random
os.system("cls")

tanulok = []
sorszam = 1
while True:
    nev = input(f"Add meg a(z) {sorszam}. tanuló nevét: ")
    sorszam+=1
    if not nev:
        break
    tanulok.append(nev)

felelo = random.choice(tanulok)
print(felelo)