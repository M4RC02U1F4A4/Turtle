import turtle
import random
import time
from random import randint as rand
screen = turtle.Screen()

turtlepower = []

ob = turtle.Turtle()
ob.speed(0)
turtle.colormode(255)
ob.hideturtle()

turtle.tracer(0, 0)

for i in range(2000):
    r = rand(0, 255)
    g = rand(0, 255)
    b = rand(0, 255)

    ob.color(r, g, b)
    ob.forward(30 + i)
    ob.left(91)

turtle.update()

turtle.done()
