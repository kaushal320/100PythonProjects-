import random
import turtle
from turtle import Turtle,Screen
t=Turtle()
t.speed("fastest")
turtle.colormode(255)
t.width(3)

def random_color():
    r= random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    color=(r,g,b)
    return color


def draw_spirograph(size_of_gap):
    for i in range(int(360/size_of_gap)):
        t.color(random_color())
        t.circle(100)
        current_heading= t.heading()
        t.setheading(current_heading+size_of_gap)

draw_spirograph(5)






s=Screen()
s.exitonclick()