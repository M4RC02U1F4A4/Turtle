import turtle
from random import randint as rand

def geom(size, lati, ob):
    for i in range(lati):
        ob.forward(size)
        ob.left(360/lati)

ob = turtle.Turtle()
ob.speed(0)
turtle.colormode(255)
ob.hideturtle()

turtle.bgcolor("black")
ob.pensize(3)
ob.left(24)

r = 0
g = 0
b = 0

turtle.tracer(0, 0)

for i in range(2000):
    geom(500, 5, ob)
    ob.forward(i/7)
    ob.left(45)
    if b < 255:
        b += 1
    else:
        b = 0
    ob.color(10, 0, b)

turtle.update()
turtle.done()
