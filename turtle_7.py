import turtle
import random
import time
from random import randint as rand

bg_color = "black"
ob = turtle.Turtle()

ob.speed(10)
turtle.colormode(255)
ob.hideturtle()
ob.pensize(2)
turtle.bgcolor(bg_color)

turtle.tracer(0, 0)

rainbowColors = ["#FF0000","#FFA600","#FFFF00", "#62FF00", "#1E56FC","#4800FF","#CC00FF","#69C5FF"]
k=0
x_start = 990
y_start = 0

ob.goto(x_start, y_start)
for i in range(720):
    for j in range(30):
        ob.color(rainbowColors[rand(0,7)])
        ob.forward(i/10)
        ob.color(bg_color)
        ob.forward(i/10)
    ob.penup()
    ob.goto(x_start, y_start)
    ob.pendown()
    ob.left(0.5)

turtle.update()
turtle.done()
