from turtle import Turtle
import random

class Food:
    def __init__(self):
        self.food_positions=[]
        self.food_positions_fixed=[]
        self.food_state=True
        for c in range (28):
            x=-280+20*c
            y=-280+20*c
            self.food_positions.append((x,y))

        self.food_positions_fixed=self.food_positions
        self.food_turtle=Turtle(shape="square")
        self.food_turtle.penup()
        self.food_turtle.color("green")     
        self.current_food_pose=random.choice(self.food_positions) 
        self.food_turtle.setposition(self.current_food_pose)
    def update_food(self):
        self.food_positions.reverse()
        self.current_food_pose=random.choice(self.food_positions)
        self.food_turtle.setposition(self.current_food_pose)
        self.food_state=True
        self.food_positions=self.food_positions_fixed
        