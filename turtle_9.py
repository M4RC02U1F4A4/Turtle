import turtle
import random
from random import randint as rand
import cmath

def collega(x, y, ob):
    for i in range(len(x)):
        x_p = x[i]
        y_p = y[i]
        for j in range(len(x)-i):
            ob.color(rand(0, 255), rand(0, 255), rand(0, 255))
            ob.penup()
            ob.goto(x_p, y_p)
            ob.pendown()
            ob.goto(x[j], y[j])

bg_color = "black"
ob = turtle.Turtle()

ob.speed(0)
turtle.colormode(255)
ob.hideturtle()
ob.pensize(2)
turtle.bgcolor(bg_color)

turtle.tracer(0, 0)
x = []
y = []
k=0

while(k<100):
    r = rand(0, 360)
    x.append(500*cmath.cos(r).real)
    y.append(500*cmath.sin(r).real)
    k += 1

collega(x, y, ob)

turtle.update()
turtle.done()
