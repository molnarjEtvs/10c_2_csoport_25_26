import os
os.system("cls")

bruttoFizetes = int(input("Add meg a bruttó fizetésed: "))
eletkor = int(input("Add meg az életkorod: "))
szja = bruttoFizetes * 0.15
if eletkor<25:
    szja = 0
tb = bruttoFizetes * 0.185
szocho = bruttoFizetes * 0.13

nettoFizetes = bruttoFizetes-szja-tb
munkKolts = bruttoFizetes + szocho

print(f"A fizetésedből levont SZJA összege: {szja} Ft, TB összeg: {tb} Ft")
print(f"A nettó fizetésed: {nettoFizetes} Ft")
print(f"A munkáltató ezt az összeget utalta el neked: {munkKolts} Ft")