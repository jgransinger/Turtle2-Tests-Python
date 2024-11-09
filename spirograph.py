import turtle as t
from turtle import *
import random

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r,g,b)
    return rgb

t.colormode(255)
brutus = Turtle()
brutus.shape("turtle")
brutus.color("dark green")

def spirograph(x):
    heading = 0
    brutus.speed(0)
    brutus.pensize(0)
    while heading < 360:
        brutus.color("black")
        brutus.pencolor(random_color())
        brutus.circle(x)
        brutus.setheading(heading)
        heading += 10

# ---------------------

spirograph(100)
spirograph(50)

screen = Screen()
screen.exitonclick()






