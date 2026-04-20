import os
os.system("cls")

try:
    vizigeny = float(input("Add meg a vízigényt: "))
    db = int(input("Add meg a darabszámot: "))
    m3dij = 218.95
    
    vizfogyasztas = (vizigeny*db)/1000
    vizkoltseg = m3dij*vizfogyasztas

    if db<1000:
        vizkoltseg *= 2
        #vizkoltseg = vizkoltseg * 2
    elif db>=1000 and db<2000:
        vizkoltseg *= 1.8
        #vizkoltseg = vizkoltseg * 1.8
    else:
        vizkoltseg *= 1.5
        #vizkoltseg = vizkoltseg * 1.5
    vizkoltseg = round(vizkoltseg,2)
    print(f"{vizfogyasztas} m3 a vízfogyasztás, ami {vizkoltseg} Ft-ba kerül.")
except:
    print("Számokat adj meg!")
