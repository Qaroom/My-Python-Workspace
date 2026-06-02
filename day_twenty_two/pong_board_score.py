from turtle import Turtle


class Pong_Score(Turtle):
    def __init__(self, shape = "classic", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)
        self.user_score=0
        self.computer_score=0
        self.font_size=48
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(50,150)
        self.write(f"{self.user_score}",move=False,align="center",font=("Courier",self.font_size,"normal"))
        self.goto(-50,150)
        self.write(f"{self.computer_score}",move=False,align="center",font=("Courier",self.font_size,"normal"))

    def update_score(self):
        self.clear()
        self.goto(50,150)
        self.write(f"{int(self.user_score)}",move=False,align="center",font=("Courier",self.font_size,"normal"))
        self.goto(-50,150)
        self.write(f"{int(self.computer_score)}",move=False,align="center",font=("Courier",self.font_size,"normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("Game over ",move=False,align="center",font=("Courier",18,"normal"))