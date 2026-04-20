def novenyRogzites():
    nevek = []
    while True:
        nev = input("Add meg a növény nevét: ").lower()
        if not nev: #if nev == ""
            break
        nevek.append(nev)
    return nevek

def novenyElemzes(novenyek:list):
    db = len(novenyek)
    print(f"Növények száma: {db} db")
    dba = 0
    for noveny in novenyek:
        if noveny.endswith('a') == True:
            dba += 1
    print(f"a-ra végződik: {dba} db")
    szoveg = ">>>".join(novenyek)
    print(f"{szoveg}")

s = novenyRogzites()
novenyElemzes(s)