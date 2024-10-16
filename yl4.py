#16.10.24 Sten-G
#Ülesanded 4
import turtle



#Ringi pindala ja Turtle
try:
    r = int(input("sisesta ringi raadius"))
    s = 3.14*r**2
    p = 2 * 3.14 * r
    print(f"Programm väljestab konsoolis: Ringi pindala on {s:.2f} ja ümbermõõt on {p:.2f}")
    turtle.circle(r*10, 360)
    turtle.done()
except:
    print("sisesta vale!")








#kingituste pakkimine
try:
    kast = 5 
    kingitusteArv = int(input("Lisa kingituste arv"))
    komplektsid = kingitusteArv//kast #täisarvu saamine
    yle = kingitusteArv % kast #jäägi saamine
    print (f"Saad teha {komplektsid} täis kinkekasti. üle jaab {yle}kingitust.")
except:
    print("lisasid koguse valesti")







#Faili allalaadimine
try:
    FailiSuurus = int(input("Sisesta faili suurus: "))
    downlKiirus = int(input("Sisesta allalaadimise kiirus: "))
    aeg = FailiSuurus/downlKiirus
    print(f"Allalaadimiseks kulub {aeg} sekundit")
except:
    print("Sa ei sisestanud täisarvu!")











#Raamatute allahindlus
ale = 0.3
hind = 12.3
kogus = int(input("Lisa raamatute kogus: "))
summa = (hind-(hind*ale)) * kogus
print(f"{kogus} raamatu hind soodustusega on {summa:.2f}$.")






#Aia pikkus
a = int(input("Lisa 1 külg: "))
b = int(input("Lisa 2 külg: "))
P = 2 * (a+b)
print(f" Aia kogu pikkus on {p} meetrit.")