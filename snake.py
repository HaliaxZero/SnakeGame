from turtle import Turtle
STARTING_POINT = [(0,0),(-20,0),(-40,0)]

class Snake:

    def __init__(self):
        self.turtles = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POINT:
            new_turtle = Turtle("square")
            new_turtle.color("white")
            new_turtle.penup()
            new_turtle.goto(position)
            self.turtles.append(new_turtle)

    def move_snake(self):
        for turtle_number in range(len(self.turtles) - 1, 0, -1):
            new_x = self.turtles[turtle_number - 1].xcor()
            new_y = self.turtles[turtle_number - 1].ycor()
            self.turtles[turtle_number].goto(new_x, new_y)
        self.turtles[0].forward(20)


