
from turtle import *
import random


def right_angle():
    brutus.forward(100)
    brutus.right(90)


def make_a_square(turtle_name, x):
    turtle_name.forward(x)
    turtle_name.right(90)
    turtle_name.forward(x)
    turtle_name.right(90)
    turtle_name.forward(x)
    turtle_name.right(90)
    turtle_name.forward(x)
    turtle_name.right(90)

def dashed_line(turtle_name, x, y):
    for num in range (y):
        turtle_name.pendown()
        turtle_name.forward(x)
        turtle_name.color(random.choice(colors))
        turtle_name.penup()
        turtle_name.forward(x)

colors = ["red", "blue", "green", "purple", "cyan", "brown", "maroon", "pink", "LimeGreen", ]
random_angle = [90, -90, 0]

brutus = Turtle()
brutus.shape("turtle")
brutus.color("dark green")

elmo = Turtle()
elmo.color("red")
elmo.shape("turtle")

def random_walk(turtle_name, x, y):
    active = True
    decisions = 0
    turtle_name.pensize(10)
    turtle_name.speed(y)
    while active:
        turtle_name.color(random.choice(colors))
        turtle_name.forward(x)
        turtle_name.right(random.choice(random_angle))
        decisions += 1
        if decisions > 500:
            active = False


random_walk(brutus, 20, 0)

screen = Screen()
screen.exitonclick()






