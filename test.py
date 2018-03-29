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

ob.goto(0, 0)
for j in range(360):
    ob.color(rainbowColors[rand(0,7)])
    ob.forward(100)
    ob.color(bg_color)
    ob.forward(50)
    ob.color(rainbowColors[rand(0,7)])
    ob.forward(100)
    ob.color(bg_color)
    ob.forward(50)
    ob.color(rainbowColors[rand(0,7)])
    ob.forward(100)
    ob.penup()
    ob.goto(0,0)
    ob.pendown()
    ob.left(1)





turtle.update()
turtle.done()
