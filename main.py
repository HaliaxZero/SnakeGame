import time
from turtle import Turtle, Screen
from snake import  Snake

screen = Screen()
screen.setup(width= 600, height=600)
screen.bgcolor("black")
screen.title("Snake Game by -Me")
gamestate = True

snake = Snake()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

while gamestate:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()





































screen.exitonclick()