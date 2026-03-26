
def macskaRogzites():
    macskok = []
    while True:
        macsk = input("Add meg a macsk nevét: ").capitalize()
        if not macsk:
            break
        if macsk not in macskok:
            macskok.append(macsk)
    return macskok

def macskaElemzes(lista:list):
    db=len(lista)
    iBetusek = []
    for n in lista:
        if n.find("i") >= 0:
            iBetusek.append(n)

    szoveg = ">>".join(iBetusek)
    print(f"{db} macska lett rogzitve\n I betuos macskak: {iBetusek}")

macskak = macskaRogzites()
macskaElemzes(macskak)