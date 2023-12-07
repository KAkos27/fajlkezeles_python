from Szemely import Szemely

szemelyek=[]
fajlom=open("teszt.txt", "r",encoding='utf-8')
fajlom.readline()
string_lista=fajlom.readlines()
fajlom.close()

for i in range(0,len(string_lista),1):
    aktsor:str=string_lista[i].strip()
    sor_lista=aktsor.split(",")
    szemely=Szemely(sor_lista[0],sor_lista[1],int(sor_lista[2]))
    szemelyek.append(szemely)

for i in range(0,len(szemelyek),1):
    print(szemelyek[i].nev,szemelyek[i].nem,szemelyek[i].kor)

import feladatok
atlageletkor=feladatok.atlageletkor(szemelyek)
print(atlageletkor)

nokszama=feladatok.nok(szemelyek)
print(nokszama)