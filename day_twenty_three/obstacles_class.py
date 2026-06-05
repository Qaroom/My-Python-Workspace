from turtle import Turtle
import random
class Obstacles:
    def __init__(self):
        self.obstacle_list=[]
        self.is_game_on=True
        self.obstacle_colors = [
            "red", "orange", "yellow", "lime",
            "green", "cyan", "blue", "purple",
            "magenta", "pink", "gold",
            "turquoise", "coral", "violet",
            "brown", "gray"
        ]

        for x in range (10,-6,-1):
            new_obstacle=Turtle()
            new_obstacle.penup()
            new_obstacle.setheading(180)
            new_obstacle.shape("square")
            new_obstacle.color(random.choice(self.obstacle_colors))
            new_obstacle.goto(random.randint(380,750),38*x)
            self.obstacle_list.append(new_obstacle)

        

    def check_accidents(self,car_pose):
        for obstacle in self.obstacle_list:
            if obstacle.distance(car_pose) <=20:
                return True
            else :
                continue

        return False 
    
    def move_obstacles(self):
        if self.is_game_on: 
            for obstacle in self.obstacle_list:
                if obstacle.xcor()<=-380:
                    obstacle.goto(380,obstacle.ycor())
                    obstacle.forward(random.randint(5,15))
                else :
                    obstacle.forward(random.randint(2,15))
        else :
            return

    def add_obstacles(self):
        if len(self.obstacle_list) <=35:

            for _ in range(5):
                new_obstacle=Turtle()
                new_obstacle.penup()
                new_obstacle.setheading(180)
                new_obstacle.shape("square")
                new_obstacle.color(random.choice(self.obstacle_colors))
                new_obstacle.goto(random.randint(380,750),random.randint(-200,380))
                self.obstacle_list.append(new_obstacle)
        else : return 
        