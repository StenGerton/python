import turtle
#sten-gerton
#08.10.24

aken=turtle.screen()
aken.setup(width=500, height=500)
aken.title("Sinilill - Sten")
turtle.speed(0)
turtle.pensize(10)

#olümpiarõngad
turtle.pencolor("green")
turtle.goto(0,-100)
turtle.left(90)
turtle.fd(200)
turtle.rt(90)

aken = turtle.Screen()
aken.setup(width = 500, height= 400)
aken.title("Sinilill - Sten")
turtle.speed("fastest")
turtle.pensize(10)

#õis
turtle.pencolor("green")
turtle.goto(0,-150)
turtle.lt(90)
turtle.fd(200)
turtle.lt(-90)
turtle.begin_fill()
turtle.color("blue", "lightblue")
turtle.circle(70)
turtle.lt(90)
turtle.end_fill()

#süda
turtle.begin_fill()
turtle.color("yellow", "yellow")
turtle.penup()
turtle.fd(45)
turtle.pendown()
turtle.rt(90)
turtle.circle(25)
turtle.end_fill()

#leht
turtle.goto(-20,-50)
turtle.lt(90)
turtle.fd(40)
turtle.lt(120)
turtle.fd(40)
turtle.lt(120)
turtle.fd(40)
turtle.lt(120)
