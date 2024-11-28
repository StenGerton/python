#Sten-Gerton Tiitmaa
#2024.11.20
import datetime
import os

#OS kasutajanimi
print(os.getlogin())
#aktiivne kataloog
print(os.getcwd())

#Skript küsib kasutajalt, mitu kataloogi ta soovib luua
#Kataloogid luuakse praegusesse töökataloogi kuupäevaga märgistatud kataloogi sees, nummerdatuna (nt “1”, “2”)
try:
    mitu = 3
    for i in range(1,mitu+1):
    y = x.strftime("%d%m%Y")
    os.mkdir(y+"_"+str(i+1))
except:
    print("Kataloogid juba olemas!")
valik = input("lisa Kataloogi nimi kustuamiseks")
print(os.lisdir)

except:
    print("sellist kataloogi ei saa kustutada!")

items = os.listdir()
for item in items:
    if os.path.isdir(item):
        print(item)

