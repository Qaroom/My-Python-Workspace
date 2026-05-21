from turtle import Screen , Turtle
from functools import partial
from threading import Timer
import random
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
snake=[]
snake_movement_state=""
snake_poses= set() 
counter=1
food_positions=[]
food_state=True

for c in range (64):
    x=-276+9*c
    y=-276+9*c
    food_positions.append((x,y))

for x in range(4):
    if x == 0:
        new_snake=Turtle(shape="triangle")
        new_snake.penup()
        new_snake.setposition(0,0)
        new_snake.color("white")
        snake.append(new_snake)
        
    else :
        new_snake=Turtle(shape="circle")
        new_snake.penup()
        new_snake.setposition(x*-18,0)
        new_snake.color("white")
        snake.append(new_snake)
        
        
        
food_turtle=Turtle(shape="square")
food_turtle.penup()
food_turtle.color("green")     
current_food_pose=random.choice(food_positions) 
food_turtle.setposition(current_food_pose)

direction = "right"

def go_up():
    global direction
    if direction != "down":
        direction = "up"

def go_down():
    global direction
    if direction != "up":
        direction = "down"

def go_left():
    global direction
    if direction != "right":
        direction = "left"

def go_right():
    global direction
    if direction != "left":
        direction = "right"

def main():
    global snake_poses
    global food_state
    global food_positions
    global current_food_pose
    if not check_conditons():
        print(snake_poses)
        snake_poses.clear()
        for i in range(len(snake)-1,0,-1):
            x = round(snake[i-1].xcor(), 2)
            y = round(snake[i-1].ycor(), 2)
            snake[i].goto(x,y)
            if i !=0:
                 snake_poses.add((x,y))
                #  print(snake_poses)
        head = snake[0]
        if direction == "up":
            head.setheading(90)
        elif direction == "down":
            head.setheading(270)
        elif direction == "left":
            head.setheading(180)
        elif direction == "right":
            head.setheading(0)
        head.forward(18)
        
        print(snake[0].position())
    else : 
        print("game over")


    if not food_state :
        food_positions.reverse()
        current_food_pose=random.choice(food_positions)
        food_positions.remove(current_food_pose)
        food_turtle.setposition(current_food_pose)
        food_state=True
        print(f"congrat you have eaten food, snake body lenth : {len(snake)}")

    if snake[0].distance(current_food_pose) < 10:
        food_state = False

        new_snake_body = Turtle(shape="circle")
        new_snake_body.penup()
        new_snake_body.color("white")

        snake.append(new_snake_body)
        # new_snake_body.setposition(snake[-1].position()-18)


    screen.ontimer(main,10)



def check_conditons():
    return True if snake[0].position() in snake_poses or check_head_pose(snake[0].position()) else False

def check_head_pose(pose):
    return False if -300 <= pose[0] <=300 and -300 <= pose[1] <=300  else True

# def move_auto():
#     new_pose=[]
#     if abs(current_food_pose[0]-snake[0].position()[0])<=10:
#         new_pose_x=snake[0].position()[0]+ 

#     pass

screen.listen()
screen.onkey(go_up,"w")
screen.onkey(go_down,"s")
screen.onkey(go_left,"a")
screen.onkey(go_right,"d")

main()
# update_snake_pose()
screen.mainloop()

