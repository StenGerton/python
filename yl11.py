#Kirjuta funktsioon pikim_sona(), mis võtab sisendiks sõnade listi ja tagastab pikima sõna pikkuse. Prindi tulemus konsooliaknasse.


import random
import turtle


sonad = ["üks", "kaks", "kolm", "kuusteist"]

def pikim_sona(a):
    pikim_sona = 0
    for sona in a:
        if len(sona)>pikim_sona:
            pikim_sona = len(sona)
        print(pikim_sona)


pikim_sona(sonad)

#Kirjuta funktsioon nimega kolm_pikimat_sona(), mis analüüsib sõnade listi ja leiab kolm kõige pikemat sõna. Lisa kontroll juhuks, kui sõnade arv pole piisav.
def kolm_pikimat_sona(a):
    uus_sonastik = {}
    for sona in a:
        uus_sonastik[sona] = len(sona)
    jar = (sorted(uus_sonastik.items(), key=lambda x:x[1], reverse=True))
    for i in range(3):
        print(jar[i][0])

kolm_pikimat_sona(sonad)


#Kirjuta funktsioon, mis kontrollib, kas kahest sõnast koosnev sõne algab sama tähega.
# print(sarnased_esitahed('Vapper Vares')) # peaks tagastama True
# print(sarnased_esitahed('Lahe Känguru')) # peaks tagastama False

def sarnased_esitahed(a):
    tykk = a.split(" ")
    if tykk[0][0].lower()==(tykk[1][0]).lower():
        return "True"
    else:
        return "False"
print(sarnased_esitahed('Vapper Vares'))
print(sarnased_esitahed('Lahe Känguru'))

# Kilpkonn – kirjutada programm, mis lubab kasutajal valida kujundite tüübi (viisnurk, ring, ruut või suvaline) ja arvu. Programm joonistab seejärel antud arvu kujundeid valitud tüübiga või juhul, kui valik on “suvaline”, valib programm ise juhuslikult kujundi tüübi iga kujundi jaoks.
# Millist kujundit soovid joonistada (viisnurk, ring, ruut, suvaline)? Suvaline
# Mitu kujundit soovid joonistada? 5
# [Joonistab 5 kujundit, igaüks juhuslikult valitud tüübiga suvalistesse kohtadesse]
# Pärast joonistamist peaks programm pakkuma võimalust sisestada uued väärtused või väljuda programmist, jättes sisendi tühjaks.

print("----------------Joonistame kujundeid----------------")
print("Vali kujundid: \n1 viisnurk, \n2 ring, \n3 ruut, \n4 suvaline")
kujundid = int(input("Sisesta number: "))
arv = int(input("Mitu kujundit tahad(1-100): "))

def viisnurk():
    pass

def ring():
    pass


def ruut(a):
    for j in range(a):
        turtle.speed(0)
        turtle.penup()
        turtle.goto(random.randint(-400,400), random.randint(-300,300))
        turtle.pendown()
        for i in range(4):
            turtle.forward (100)
            turtle.left(90)
    print("Valisid ruudu")

def suvaline():
    pass

if kujundid == 1:
    viisnurk()
elif kujundid == 2:
    ring()
elif kujundid == 3:
    ruut(arv)
else:
    suvaline()


turtle.done()

def suvaline(k):
    for i in range(k):
         my_list = [viisnurk,ring,ruut]
         random.choise(my_list)(1)
def viisnurk(k):
    print("Joonistan Viisnurga")   

def ring(k):
    print("Joonistan ringi")   

def ruut(k):
    print("Joonistan ruudu")    
    turtle.speed(0)
    for j in range (k):
        turtle.penup()
        turtle.goto(random.radiant(-400,400),random.radiant)
                                