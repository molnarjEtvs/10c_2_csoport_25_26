import os,random
os.system("cls")

oszthato2 = []
oszthato3 = []
oszthato5 = []

for _ in range(30):
    vszam = random.randint(300,1500)
    if vszam%2==0:
        oszthato2.append(vszam)

    if vszam%3==0:
        oszthato3.append(vszam)

    if vszam%5==0:
        oszthato5.append(vszam)

print(oszthato2)
print(oszthato3)
print(oszthato5)
    