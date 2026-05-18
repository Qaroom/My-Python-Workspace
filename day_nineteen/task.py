from turtle import Turtle, Screen
import random

turtle_list = {}

screen = Screen()

class MultiTurtle:
    def __init__(self):
        self.turtle = Turtle()
        self.turtle.shape("turtle")
        self.turtle.penup()
        self.turtle.setpos(-200, random.randint(-200, 200))

    def turtle_movement(self):
        self.turtle.forward(random.randint(0, 30))

    def check_movement(self):
        return self.turtle.xcor() >= 200


for i in range(5):
    turtle_list[i] = MultiTurtle()


race_on = True

while race_on:

    for turtle_obj in turtle_list.values():

        if turtle_obj.check_movement():
            race_on = False
            print("Race finished!")
            print(f"the winer of race is {turtle_obj}")
            break

        turtle_obj.turtle_movement()


screen.exitonclick()