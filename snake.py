from turtle import Turtle
STARTING_POINT = [(0,0),(-20,0),(-40,0)]
Up = 90
Right = 0
Down = 270
Left = 180

class Snake:

    def __init__(self):
        self.turtles = []
        self.create_snake()
        self.head = self.turtles[0]


    def create_snake(self):
        for position in STARTING_POINT:
            self.add_snake(position)

    def move_snake(self):
        for turtle_number in range(len(self.turtles) - 1, 0, -1):
            new_x = self.turtles[turtle_number - 1].xcor()
            new_y = self.turtles[turtle_number - 1].ycor()
            self.turtles[turtle_number].goto(new_x, new_y)
        self.turtles[0].forward(20)

    def right(self):
        if self.head.heading() != Left:
            self.turtles[0].setheading(Right)

    def left(self):
        if self.head.heading() != Right:
            self.turtles[0].setheading(180)

    def up(self):
        if self.head.heading() != Down:
            self.turtles[0].setheading(90)

    def down(self):
        if self.head.heading != Up:
            self.turtles[0].setheading(270)

    def extend(self):
        #add new segment to snake
        self.add_snake(self.turtles[-1].position())

    def add_snake(self,position):

        new_turtle = Turtle("square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(position)
        self.turtles.append(new_turtle)