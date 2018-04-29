import turtle
import random
from random import randint as rand
import cmath



bg_color = "black"
ob = turtle.Turtle()

ob.speed(10)
turtle.colormode(255)
ob.hideturtle()
ob.pensize(1)
turtle.bgcolor(bg_color)
ob.color("white")

turtle.tracer(0, 0)

x = []
y = []

k = -500
z = -500
a = -500
while(k < 500):
    while(z < 500):
        while(a < 500):
            x.append(k)
            y.append(cmath.sqrt((-1)*(1-a**2-k**2-z**2)).real)
            a += 10
        a = -500
        z += 10
    z = -500
    k += 10

print(x, y)

ob.penup()
ob.goto(x[0], y[0])
ob.pendown()
for i in range(len(x)):
    ob.goto(x[i], y[i]-400)
    print(len(x)-i)


turtle.update()
turtle.done()
