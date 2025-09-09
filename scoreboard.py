from turtle import  Turtle
ALIGNMENT = "center"
FONT = ("Courier" ,24 ,"normal")
class Highscore(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 250)
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)


    def screen_clear(self):
        self.clear()

    def update_score(self):
        self.write(f"Score: {self.score}" , align=ALIGNMENT, font=FONT)

    def counter(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over!" , align=ALIGNMENT, font=FONT)
