import turtle
import random

aken = turtle.Screen()
aken.bgcolor("lightblue")
aken.setup(width=600, height=600)
aken.tracer(0)

# ristkülik
ristkylik = turtle.Turtle()
ristkylik.shape("square")
ristkylik.shapesize(stretch_wid=1, stretch_len=5)
ristkylik.penup()
ristkylik.color("black")
ristkylik.goto(ristkylik.xcor(), -250)

# ring
ring = turtle.Turtle()
ring.shape("circle")
ring.penup()
ring.speed('fastest')
ring.setheading(random.randint(0, 360))

# skoor
skoor = 0
# kiirused
ristkyliku_kiirus = 20
kiirus = 10

# ristküliku funktsioonid
def liigu_vasakule():
    x = ristkylik.xcor()
    if x > -280:
        ristkylik.setx(x - ristkyliku_kiirus)

def liigu_paremale():
    x = ristkylik.xcor()
    if x < 280:
        ristkylik.setx(x + ristkyliku_kiirus)

# ringi funktsioonid
def peegelda_porkumisel():
    nurk = ring.heading()
    if ring.xcor() >= 300 or ring.xcor() <= -300:
        uus_nurk = 180 - nurk
        if uus_nurk < 0:
            uus_nurk += 360
        ring.setheading(uus_nurk)
    if ring.ycor() >= 300:
        uus_nurk = 360 - nurk
        ring.setheading(uus_nurk)
    if ring.ycor() <= -300:
        print("Game Over")
        turtle.bye()
        aken.ontimer(ring_liigu, 0)
        
def kokkuporge():
    global skoor
    skoor+=1
    print(f"skoor:{skoor} ")



def ring_liigu():
    ring.forward(kiirus)
    peegelda_porkumisel()
    aken.update()
    aken.ontimer(ring_liigu, 20)

    #tuvasta kokkuporge alusega
    if  ring.ycor() < -220 and (ristkylik.xcor() < ring.xcor()+50 and ristkylik.xcor() > ring.xcor()-50):
        kokkuporge()
        nurk = ring.heading()
        uus_nurk = 360 - nurk
        ring.setheading(uus_nurk)   
    
def kokkuporge():
    global skoor
    global kiirus
    turtle.goto(-250, 250)
    turtle.clear()
    turtle.hideturtle()
    skoor+=1
    kiirus+=2
    print(f"Skoor:{skoor}")
    aken.write(skoor, font=("Arial",20, "normal"))


# klaviatuurile reageerimine
aken.listen()
aken.onkeypress(liigu_vasakule, "Left")
aken.onkeypress(liigu_paremale, "Right")

ring_liigu()

aken.mainloop()