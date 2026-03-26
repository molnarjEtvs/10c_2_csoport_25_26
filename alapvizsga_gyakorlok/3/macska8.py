import os
os.system("cls")

kor=int(input("Add meg a macska életkorát: "))
suly=float(input("Add meg a macska súlyát: "))
adag = 65
etelmennyiseg = suly*adag*7
if kor < 2:
    kcal = 80
elif kor >= 2 and kor < 5:
    kcal = 95
else:
    kcal = 110
mozgasigeny = suly*kcal
mozgasigeny = round(mozgasigeny,1)
print(f"A macska napi mozgás igénye: {mozgasigeny}kcal, és heti étel szükséglete: {etelmennyiseg}gramm")