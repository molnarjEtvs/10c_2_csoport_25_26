import os,random
os.system("cls")

def jelszo_generalas(hossz:int):
    karakterek = "0123456789qwertzuiopasdfghjklyxcvbnm"
    karakterek_lista = list(karakterek)
    jelszo = ""
    for _ in range(hossz):
        jelszo += random.choice(karakterek_lista)
    return jelszo

def vizsgalt_jelszo(jelszo:str):
    if len(jelszo)<5:
        print("Gyenge jelszó")
    elif len(jelszo)>=5 and len(jelszo)<=8:
        print("Közepes jelszó")
    else:
        print("Erős jelszó")

j = jelszo_generalas(4)
vizsgalt_jelszo(j)
