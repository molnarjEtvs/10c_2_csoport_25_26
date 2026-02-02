def fizetes_szamitas(oraszam:int,oraber:float,tulora_szorzo:float = 1.5):
    if oraszam<=40:
        fizetes = oraber*oraszam
    else:
        fizetes = oraber*40
        tulorafizetes = (oraszam-40)*(oraber*tulora_szorzo)
        fizetes += tulorafizetes
    return fizetes
