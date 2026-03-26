def bolygoRogzites():
    bolygok = []
    while True:
        bolygo = input("Adj meg egy bolygót:").capitalize()
        if not bolygo:
            break
        bolygok.append(bolygo)
    return bolygok
def bolygoElemzes(bolygok:list):
    db = len(bolygok)
    print(f"{db} bolygó került rögzítésre")

    dbn=0
    for bolygo in bolygok:
        if len(bolygo)== 4:
            dbn+=1
    print(f"4 betusek szama {dbn} db")
    szoveg="_$_".join(bolygok)
    print(f"A rögzített bolygók: {szoveg}")

v = bolygoRogzites()
bolygoElemzes(v)