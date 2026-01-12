import os
os.system("cls")

gyumolcsok = []
while True:
    gyumolcs = input("Add meg gyümölcs nevet: ")
    gyumolcs = gyumolcs.capitalize()
    if not gyumolcs:
        break
    gyumolcsok.append(gyumolcs)

print(gyumolcsok)