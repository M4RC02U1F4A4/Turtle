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
ob.left(36)
for i in range(2000):
    r = rand(0, 255)
    g = rand(0, 255)
    b = rand(0, 255)

    ob.color(r, g, b)
    geom(20 + i, 5, ob)
    ob.left(90)

turtle.done()
