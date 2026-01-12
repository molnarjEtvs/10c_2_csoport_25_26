import os,random
os.system("cls")

szamok = []
db = int(input("darabszám: "))
start = int(input("Tól érték: "))
stop = int(input("Ig- érték: "))

for _ in range(db):
    vszam = random.randint(start,stop)
    szamok.append(vszam)
print(szamok)