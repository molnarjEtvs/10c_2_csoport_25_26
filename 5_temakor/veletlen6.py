import os,random
os.system("cls")


tipus = input("Melyik L vagy E?:")

if tipus == "L":
    szam = random.uniform(8,88)
elif tipus == "E":
    szam = random.randint(8,88)
else:
    szam = "Nem tudtam értelmezni"

print(szam)