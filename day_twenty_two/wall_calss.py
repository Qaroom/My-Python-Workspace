from turtle import Turtle


class WallClass:
    def __init__(self):
        self.control_number=0
        self.wall_list=[]
        self.walls_posetions=[]
        self.state_control=False
        for x in range(2,-3,-1):
            new_wall=Turtle()
            new_wall.speed("fastest")
            new_wall.penup()
            new_wall.setposition(580,20*x)
            new_wall.color("white")
            new_wall.shape("square")
            # new_wall.position()
            # new_wall.distance()
            self.wall_list.append(new_wall)
            self.wall_list

    def check_distance(self,distance=(0,0)):
        if not self.state_control :
            for wall in self.wall_list:
                if wall.distance(distance) <=15:  
                    self.state_control=True 
                    return True
                else :
                    continue
            # self.state_control=False
            return False
        else :
            if self.wall_list[0].distance(distance)>100:
            
                self.state_control=False
            return False
    
    def move_wall_auto(self,ball_pose=(0,0)):
        if ball_pose[0]<0:
            for x ,wall in zip(range(2,-3,-1), self.wall_list):
                wall.goto(wall.xcor(),ball_pose[1]+x*20)
        else :
            return
               
            
    def update_wall_posetion(self):
        for wall in self.wall_list:
            x=round(wall.xcor(),1)
            y=round(wall.ycor(),1)
            self.walls_posetions.append((x,y))
        # print(self.walls_posetions)
        return self.walls_posetions

    def set_wall_pose_to_another_side(self):
        for x in range(len(self.wall_list)):
            self.wall_list[x].goto(-590,self.wall_list[x].ycor())

    def reset_speed_of_wall(self):
        for x in range(len(self.wall_list)):
            self.wall_list[x].speed(5)

    def move_walls_up(self):
        if self.wall_list[0].ycor()<285:
            for x in range(len(self.wall_list)):

                self.wall_list[x].setheading(90)
                self.wall_list[x].forward(20)
        else :
            return
            
    def move_walls_down(self):
        if self.wall_list[-1].ycor()>-285:
            for x in range(len(self.wall_list)):
                self.wall_list[x].setheading(-90)
                self.wall_list[x].forward(20)

        else :
            return
        
    