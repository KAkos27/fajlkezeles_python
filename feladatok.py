def atlageletkor(lista):
    osszeg=0
    for i in range(0,len(lista),1):
        osszeg+=lista[i].kor
    
    return osszeg/len(lista)
def nok(lista):
    mennyiseg=0
    for i in range(0,len(lista),1):
        nem = lista[i].nem
        if nem == " nő":
            mennyiseg+=1
    return mennyiseg


    
        
