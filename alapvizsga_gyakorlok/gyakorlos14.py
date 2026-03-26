import os
os.system("cls")

def  konyvRogzites():
    konyvek = []
    while True:
        konyvcim  = input("irj egy konyvcimet: ")
        if not konyvcim:
            break
        konyvek.append(konyvcim.capitalize())
    return konyvek

def konyvElemzes(lista:list):
    db=len(lista)
    dbv=0
    for konyv in lista:
        if konyv.find("b") > -1:
            dbv +=1
    uelott = lista[-2]
    azBetusek = []
    for egyKonyv in lista:
        if  egyKonyv.startswith("A") == True and egyKonyv.endswith("z") == True:
            azBetusek.append(egyKonyv)
    
    szoveg = ", ".join(azBetusek)
    print(f"{szoveg}")    
    print(f"darabszám: {db} db")
    print(f"Utolsó előtti: {uelott}")


a = konyvRogzites()
konyvElemzes(a)
    


