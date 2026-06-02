from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self, shape = "classic", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0,270)
        self.score=0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"score : {self.score}", move=False , align="center",font=("Courier", 18 , "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("Game over", move=False , align="center",font=("Courier", 18 , "normal"))
    
    def refrash_score(self):
        self.score +=1
        self.update_score()
