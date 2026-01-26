import os
os.system("cls")

csunyak = ["geci","ribanc","kurva"]
szepek = ["sperma","örömlány","prostituált"]

mondat = input("Adj meg egy mondatot: ")
for i in range(len(csunyak)):
    mondat = mondat.replace(csunyak[i],szepek[i])

print(mondat)