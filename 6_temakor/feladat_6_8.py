import os
os.system("cls")

lista = []

while True:
    elem = input("Adj meg szövegszámot: ")
    if elem.isalnum() == False:
        break
    lista.append(elem)

print(lista)