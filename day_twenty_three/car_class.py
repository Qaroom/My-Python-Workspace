from turtle import Turtle


class CarObject(Turtle):
    def __init__(self, shape = "turtle", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)
        self.penup()
        self.setheading(90)
        self.goto(0,-380)
        self.color("red")
        self.penup()

        self.move_step=20
    def move_up(self):
        new_y=self.ycor()+self.move_step
        self.goto(self.xcor(),new_y)

    def move_down(self):
        new_y=self.ycor()-self.move_step
        self.goto(self.xcor(),new_y)

    def move_right(self):
        new_x=self.xcor()+self.move_step
        self.goto(new_x,self.ycor())
    
    def move_left(self):
        new_x=self.xcor()-self.move_step
        self.goto(new_x,self.ycor())

    def go_to_starting_posetion(self):
        self.goto(0,-380)

    

