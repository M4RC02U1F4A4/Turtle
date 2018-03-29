import turtle
from random import randint as rand

ob = turtle.Turtle()
ob.speed(0)
turtle.colormode(255)
ob.hideturtle()

turtle.bgcolor("black")
ob.pensize(9)

r = 0
g = 0
b = 255

turtle.tracer(0, 0)

for i in range(20000):
    if(r > 0 and b == 0):
        r -= 1
        g += 1
    if(g > 0 and r == 0):
        g -= 1
        b += 1
    if(b > 0 and g == 0):
        r += 1
        b -= 1

    ob.color(r, g, b)
    ob.forward(i/100)
    ob.left(7)

turtle.update()
turtle.done()
