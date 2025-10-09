import os
os.system("cls")

jegyek = []

while True:
    jegy = int(input("Add meg a jegyet: "))
    if jegy == 0:
        break
    jegyek.append(jegy)

legjobbJegy = max(jegyek)
legrosszabbJegy = min(jegyek)
db = len(jegyek)
atlag = sum(jegyek)/db

print(f"Legjobb: {legjobbJegy}\nLegrosszabb:{legrosszabbJegy}\nJegyek száma:{db} db\nÁtlag:{atlag}")