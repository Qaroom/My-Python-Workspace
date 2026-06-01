from turtle import Turtle

class PongBall(Turtle):
    def __init__(self, shape = "classic", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)

        self.penup()
        self.color("white")
        self.setposition(0,0)
        self.shape("circle")
        self.first_distance=0.0

    def move_pong_ball(self):
        if self.first_distance <= self.distance(0,0) :
             self.setheading(self.heading()+60)
             self.forward(20)  
             self.first_distance=self.distance(0,0)      

        else : 
             self.setheading(self.heading()-60)
             self.forward(20)  
             self.first_distance=self.distance(0,0)