from turtle import Turtle 

class ScoreBoard(Turtle):
    def __init__(self, shape = "classic", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)

        self.hideturtle()
        self.color("green")
        self.penup()
        self.score=0
        self.life_number=7
        self.update_score()
    def update_score(self):
        self.clear()
        self.goto(-380,-380)
        self.write(f"Your score is : {self.score}",move=False,align="left",font=("Courier" , 12 , "normal"))
        self.goto(380,-380)
        self.write(f"{self.life_number} life remaind",move=False,align="right",font=("Courier" , 12 , "normal"))

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"Game Over",move=False,align="center",font=("Courier" , 48 , "normal"))

    def winner(self):
        self.clear()
        self.goto(0,0)
        self.write(f"You Win",move=False,align="center",font=("Courier" , 48 , "normal"))
