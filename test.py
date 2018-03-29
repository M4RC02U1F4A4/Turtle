import turtle
import random
import time
from random import randint as rand
import cmath

def collega(x_p, y_p, ob, x, y):
    r, g, b = 0, 255, 0
    for i in range(int(len(x)/2)):
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
        ob.penup()
        ob.goto(x_p, y_p)
        ob.pendown()
        ob.goto(x[i], y[i])
    r, g, b = 0, 255, 0
    i = len(x)-1
    while(i>=len(x)/2):
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
        ob.penup()
        ob.goto(x_p, y_p)
        ob.pendown()
        ob.goto(x[i], y[i])
        i -= 1


bg_color = "black"
ob = turtle.Turtle()

ob.speed(0)
turtle.colormode(255)
ob.hideturtle()
ob.pensize(2)
turtle.bgcolor(bg_color)
ob.color("black")

turtle.tracer(0, 0)
x1 = []
y1 = []
x2 = []
y2 = []
k=-400
while(k<400):
    #r = rand(0, 360)
    x1.append(2*k)
    y1.append(50*cmath.cos(k/12).real-700)
    k += 1.1

k=-400
while(k<400):
    #r = rand(0, 360)
    x2.append(2*k)
    y2.append(-50*cmath.cos(k/12).real+700)
    k += 1.1

ob.penup()
ob.goto(x1[0], y1[0])
ob.pendown()
for i in range(len(x1)):
    ob.goto(x1[i], y1[i])

ob.penup()
ob.goto(x2[0], y2[0])
ob.pendown()
for i in range(len(x1)):
    ob.goto(x2[i], y2[i])

collega(0, 400, ob, x1, y1)
collega(0, -400, ob, x2, y2)

turtle.update()
turtle.done()
