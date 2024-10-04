from math import *
#Sen-Gerton Tiitmaa
#30.09.24
#harjutus 02


#kolmnurga ümbermõõt
a = int(input("lisa arv: "))
b = int(input("lisa arv: "))
c = int(input("lisa arv: "))
p=a+b+c
print("kolmnurga ümbermõõt on", p, "ühikut")




#toote hind
tootehind = 36.75
ale = 0.4
soodushind = tootehind - (tootehind * ale)
kogus = 3
kokku = soodushind * kogus
print(kokku)



#5. pitsa
hind = 14.19
hind1 = hind / 3
print("igaüks maksab", hind1, "€")






#6 rulluisutajad 90km/h
kiirus = 29.9
aeg=24/60
dist= kiirus * aeg
print("Rulluisutaja jõuab:",dist,"km kaugusele")





#hüpotenuus **
a,b = 16,9
c = sqrt(a**2 + b**2)
print("Hüpotenuus on:",c)






#kütusekulu arvutamine

#Ajateisendus // %
aeg = int(input("Lisa aeg minutites: "))
aeg = 72
h = aeg/60
m = aeg % 60
print(h,":",m)









l = int(input("Lisa tangitud liitrid: "))
km = int(input("Lisa läbitud kilomeetrid: "))
kytusekulu = l/(km/100)
print("Sinu kütusekulu",kytusekulu)

#arvusüsteemid
arv = int(input("Lisa arv: "))
kahend = bin(arv)
kuust = hex(arv)
print("Sinu teisendused on: ",kahend, "ja",kuust)