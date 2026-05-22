from turtle import Turtle


class Snake: 
    def __init__(self):
        self.snake=[]
        self.direction="right"
        self.snake_poses=set()
        for x in range(4):
            if x == 0:
                new_snake=Turtle(shape="triangle")
                new_snake.penup()
                new_snake.speed(5)
                new_snake.setposition(0,0)
                new_snake.color("white")
                self.snake.append(new_snake)
                
            else :
                new_snake=Turtle(shape="circle")
                new_snake.penup()
                new_snake.setposition(x*-20,0)
                new_snake.color("white")
                self.snake.append(new_snake)
        

    def rewrite_head_pose(self):
        x=round(self.snake[0].position()[0],1)
        y=round(self.snake[0].position()[1],1)
        return (x , y)
    
    def new_snake_body(self): 
        new_snake_body = Turtle(shape="circle")
        new_snake_body.penup()
        new_snake_body.color("white")
        self.snake.append(new_snake_body)
    def go_up(self):
    
        if self.direction != "down":
            self.direction = "up"

    def go_down(self):
        
        if self.direction != "up":
           self.direction = "down"

    def go_left(self):
        
        if self.direction != "right":
            self.direction = "left"

    def go_right(self):
        
        if self.direction != "left":
            self.direction = "right"

    def new_snake_body(self):
        new_snake_body = Turtle(shape="circle")
        new_snake_body.penup()
        new_snake_body.color("white")
        self.snake.append(new_snake_body)

    def check_conditons(self):
        return True if self.rewrite_head_pose() in self.snake_poses or self.check_head_pose(self.rewrite_head_pose()) else False

    def check_head_pose(self,pose):
        return False if -300 <= pose[0] <=300 and -300 <= pose[1] <=300  else True
    
    def update_snake_poses(self):
        for i in range(len(self.snake)-1,0,-1):
            x = round(self.snake[i-1].xcor(), 2)
            y = round(self.snake[i-1].ycor(), 2)
            self.snake[i].goto(x,y)
            if i !=0:
                 self.snake_poses.add((x,y))
    