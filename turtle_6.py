import turtle
import random
import time
from random import randint as rand

ob = turtle.Turtle()
ob.speed(0)
turtle.colormode(255)
ob.hideturtle()
k=15
ob.pensize(k)
turtle.tracer(0, 0)

for i in range(2000):
    r = rand(0, 255)
    g = rand(0, 255)
    b = rand(0, 255)
    ob.color(r, g, b)
    if i%200 == 0:
        k += 1
        ob.pensize(k)
    ob.forward(0 + i)
    ob.left(91)

turtle.update()

turtle.done()
