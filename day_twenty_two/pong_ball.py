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
        # self.setheading(-90)
        # print(self.heading())
        # self.reached_to_computer_wall=False
    def update_pose_of_pong(self):
        x=round(self.xcor(),1)
        y=round(self.ycor(),1)
        return (x,y)
    def move_pong_ball(self,direction):
        if direction=="CW" :
             self.setheading(self.heading()+random.randint(40,45)+self.second_heading_value)
            #  self.forward(20)  
             self.first_distance=self.distance(0,0)      

        elif direction=="CCW":
             self.setheading(self.heading()-random.randint(40,45)-self.second_heading_value)
            #  self.forward(20)  
             self.first_distance=self.distance(0,0)

        else :
            self.forward(20)

    def check_pose_of_pong(self,user_state=False,computer_state=False):
        
        if self.ycor() >=270  :
            if not self.reached_to_user_wall:
                 self.move_pong_ball("CCW")
            else :
                self.move_pong_ball("CW")
        elif self.ycor() <=-270:
            if not self.reached_to_user_wall:
                self.move_pong_ball("CW")
            else :
                self.move_pong_ball("CCW")
        if user_state: 
            self.move_pong_ball("CW")
            self.reached_to_user_wall=True
            # print("pong ball have been reached to right side")
        elif computer_state:
            self.move_pong_ball("CCW")
            print("hello")
            self.reached_to_user_wall=False