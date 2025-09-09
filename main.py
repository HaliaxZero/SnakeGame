import time
from turtle import Screen
from snake import  Snake
from food import  Food
from scoreboard import Highscore

screen = Screen()
screen.setup(width= 600, height=600)
screen.bgcolor("black")
screen.title("Snake Game by -Me")
gamestate = True

snake = Snake()
food = Food()
score = Highscore()




screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

while gamestate:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

    # collision food
    if snake.head.distance(food) <= 13:
        food.refresh()
        score.counter()
        snake.extend()

    #collision wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        gamestate = False
        score.game_over()

    #detect tail collision
    for turtles in snake.turtles[1:]:
        if snake.head.distance(turtles) <10:
            gamestate = False
            score.game_over()



































screen.exitonclick()