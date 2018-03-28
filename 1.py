import turtle
from random import randint as rand

ob = turtle.Turtle()
ob.speed(0)
turtle.colormode(255)
ob.hideturtle()

turtle.bgcolor("black")

for i in range(2000):
    r = rand(0, 255)
    g = rand(0, 255)
    b = rand(0, 255)

    ob.color(r, g, b)
    ob.forward(30 + i)
    ob.left(91)

turtle.done()
