import os
import random
os.system("cls")

class Pokemon:

    def __init__(self, dex:int, nev:str, ero:float):
        self.dex = dex
        self.nev = nev
        self.ero = ero

    def beallitas(self):
        self.ugrasimagassag = self.ero *3 * 0.885
    
    def kepessegvalasztas(self):
        lista = ["parolgas", "tuzhanyas", "loves", "gurulas"]
        self.kepesseg = random.choice(lista)

    def csoportositas(self,kor:int):
        if kor >= 15:
            self.csoport = "idos"
        else:
            self.csoport = "fiatal"

pokemonok = []

with open("pokemonLista.txt","r",encoding="UTF-8") as f:
    for sor in f:
        adat = sor.strip().split(",")
        pokemon1= Pokemon(int(adat[0]),adat[1],float(adat[2]))
        pokemon1.beallitas()
        pokemon1.kepessegvalasztas()
        pokemon1.csoportositas(random.randint(1,50))
        pokemonok.append(pokemon1)
        del pokemon1

with open("pokeadat.txt","w",encoding="utf-8") as a:
    for egypoke in pokemonok:
        a.write(f"DEX: {egypoke.dex} \nNév:{egypoke.nev}\nErő/ugrási magasság:{egypoke.ero} KP / {egypoke.ugrasimagassag} m \nKépesség/csoport: {egypoke.kepesseg} / {egypoke.csoport}\n********************************\n")