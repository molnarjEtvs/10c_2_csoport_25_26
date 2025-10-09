import os
os.system("cls")

#1 megoldás
szo = ""
while szo != "STOP":
    szo = input("Adj meg egy szót: ")

print("A program futásának vége.")

#2megoldás

while True:
    szo = input("Adj meg egy szót: ")
    if szo == "STOP":
        break

print("A program futásának vége.")
