import os
os.system("cls")

def fagylaltNevek():
    fagylaltok = []
    while True:
        fagyi = input("Add meg a fagyi nevét: ")
        if not fagyi:
            break
        fagylaltok.append(fagyi)
    return fagylaltok

def statisztikak(fagyik:list):
    db = len(fagyik)
    print(f"{db} féle fagylalt kapható")
    vegan_db = 0
    for fagyi in fagyik:
        if fagyi.lower().find("vegán")>-1:
            vegan_db += 1
    print(f"Ebből vegán: {vegan_db} db")

f = fagylaltNevek()
statisztikak(f)