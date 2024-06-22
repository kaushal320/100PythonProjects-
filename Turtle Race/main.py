from turtle import Turtle,Screen
import random
is_race_on=False
screen=Screen()
screen.setup( width=500,height=400)
user_bet=screen.textinput(title="Make your bet",prompt="Which turtle will win the race?")


colors=['red','blue','green','yellow','purple','orange']
y_postion = [-100, -60, -20, 20, 60, 100]
all_turtle=[]
#Create 6 turtles
for turtle_index in range(6):
    new_turtle=Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_postion[turtle_index])
    all_turtle.append(new_turtle)
if user_bet:
    is_race_on=True

#for winner
while is_race_on:
    for turtle in all_turtle:
        # 230 is 250 - half the width of the turtle.
        if turtle.xcor()>230:
            is_race_on=False
            new_color=turtle.pencolor()
            if new_color==user_bet:
                print(f"you have won! {new_color} is the winner")
            else:
                print(f"you have lost! {new_color} is the winner")
        # Make each turtle move a random amount.
        random_distance=random.randint(0,10)
        turtle.forward(random_distance)




screen.exitonclick()