from turtle import Turtle
import random

class PongBall(Turtle):
    def __init__(self, shape = "classic", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)
        self.last_y_pose=0
        self.penup()
        self.second_heading_value=0
        self.color("white")
        self.setposition(0,0)
        self.shape("circle")
        self.first_distance=0.0
        self.reached_to_user_wall=False
        self.x_step=10
        self.y_step=10

    def update_pose_of_pong(self):
        x=round(self.xcor(),1)
        y=round(self.ycor(),1)
        return (x,y)
    
    def move_pong_ball(self):
        new_x=self.xcor()+self.x_step
        new_y=self.ycor()+self.y_step
        self.goto(new_x,new_y)

    def reset_pong_posetion(self):
        self.bounce_x()


    
    def bounce_x(self):
        self.x_step = self.x_step *-1

    def bounce_y(self):
        self.y_step=self.y_step*-1


