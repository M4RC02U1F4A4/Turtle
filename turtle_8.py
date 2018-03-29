import turtle
import random
import time
from random import randint as rand
import cmath

bg_color = "white"
ob = turtle.Turtle()

ob.speed(10)
turtle.colormode(255)
ob.hideturtle()
ob.pensize(49)
turtle.bgcolor(bg_color)

turtle.tracer(0, 0)

x_start = 0
y_start = 0
pos = []

a = 15
b = 15

k = 0
while(k<75):
    pos.append(((a+(b*k))*cmath.cos(k).real, (a+(b*k))*cmath.sin(k).real))
    k +=0.08
r, g, b = 0, 0, 255
for i in range(len(pos)):
    #ob.color(rainbowColors[rand(0,7)])
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
    ob.goto(pos[i])
ob.penup()
ob.goto(x_start, y_start)
ob.pendown()
turtle.update()
turtle.done()
