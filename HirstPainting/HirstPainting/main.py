# import colorgram
# rgb=[]
# colors=colorgram.extract('20_001.jpg',25)
# for color in colors:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
#     new_color=(r,g,b)
#     rgb.append((new_color))
# print(rgb)
import random
import turtle
from turtle import Turtle,Screen
t=Turtle()
t.speed("fastest")

colorlist=[(199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (222, 224, 227), (186, 158, 53), (6, 57, 83),
 (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53),
 (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155), (179, 201, 186), (172, 153, 159), (212, 183, 177),
 (176, 198, 203)]

turtle.colormode(255)
t.setheading(225)
t.penup()
t.hideturtle()
t.forward(250)
t.setheading(0)
no_of_dot=101
for count in range(1,no_of_dot):

    t.dot(20,random.choice(colorlist))
    t.forward(50)
    if count%10==0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)






screen=Screen()
screen.exitonclick()

