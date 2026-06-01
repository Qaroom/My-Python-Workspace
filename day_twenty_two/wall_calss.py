from turtle import Turtle


class WallClass:
    def __init__(self):
        
        self.wall_list=[]
        for x in range(2,-3,-1):
            new_wall=Turtle()
            new_wall.speed("fastest")
            new_wall.penup()
            new_wall.setposition(580,20*x)
            new_wall.color("white")
            new_wall.shape("square")
            
            
            self.wall_list.append(new_wall)


    def set_wall_pose_to_another_side(self):
        for x in range(len(self.wall_list)):
            self.wall_list[x].goto(-590,self.wall_list[x].ycor())

    def reset_speed_of_wall(self):
        for x in range(len(self.wall_list)):
            self.wall_list[x].speed(5)

    def move_walls_up(self):
        if self.wall_list[0].ycor()<280:
            for x in range(len(self.wall_list)):

                self.wall_list[x].setheading(90)
                self.wall_list[x].forward(20)
        else :
            return
            
    def move_walls_down(self):
        if self.wall_list[-1].ycor()>-280:
            for x in range(len(self.wall_list)):
                self.wall_list[x].setheading(-90)
                self.wall_list[x].forward(20)

        else :
            return
        
    