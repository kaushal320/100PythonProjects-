from turtle import Turtle
STARTING_POSITIONS =[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=20
UP=90
DOWN=270
LEFT=180
RIGHT=0
class Snake:
    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head=self.segment[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)



    def add_segment(self,position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segment.append(new_segment)


    def extend(self):
        self.add_segment(self.segment[-1].position())

    def move(self):
        for segment_number in range(len(self.segment) - 1, 0, -1):
            new_x_cor = self.segment[segment_number - 1].xcor()
            new_y_cor = self.segment[segment_number - 1].ycor()
            self.segment[segment_number].goto(new_x_cor, new_y_cor)
        self.head.forward(MOVE_DISTANCE)


    def up(self):
        if self.head.heading() !=DOWN:
            self.head.setheading(UP)


    def down(self):
       if self.head.heading() !=UP:
           self.segment[0].setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.segment[0].setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.segment[0].setheading(RIGHT)