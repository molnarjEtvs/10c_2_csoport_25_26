import os
os.system("cls")

mondat = input("Adj meg egy mondatot: ")
szo = input("Adj meg egy szót: ")

if mondat.startswith(szo) == True:
    print("kezdődik")
elif mondat.endswith(szo) == True:
    print("végződik")
else:
    print("nincs benne")