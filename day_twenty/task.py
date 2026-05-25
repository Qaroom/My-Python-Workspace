from turtle import Screen 
from snake_class import Snake
from food_class import Food
from scoreboard import ScoreBoard
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
speed=300
snake=Snake()
food_turtle=Food()
scoreboard=ScoreBoard()
def main():
    screen.update()
    snake.direction_update()
    global speed
    if not snake.check_conditons():
        # print(snake.snake_poses)
        snake.snake_poses.clear()
        snake.update_snake_poses()
        head = snake.snake[0]
        if snake.direction == "up":
            head.setheading(90)
        elif snake.direction == "down":
            head.setheading(270)
        elif snake.direction == "left":
            head.setheading(180)
        elif snake.direction == "right":
            head.setheading(0)
        head.forward(20)


        
        # print(snake.rewrite_head_pose())
    else : 
        scoreboard.game_over()
    
    
    if not food_turtle.food_state :
        for pose in snake.snake_poses:
            if pose in food_turtle.food_positions:
                food_turtle.food_positions.remove(pose)
        food_turtle.update_food()
        print(f"congrat you have eaten food, snake body lenth : {len(snake.snake)}")
        speed -=20
    if snake.snake[0].distance(food_turtle.food_turtle) < 10:
        food_turtle.food_state = False
        snake.new_snake_body()
        scoreboard.refrash_score()
    screen.ontimer(main,150)


screen.listen()
screen.onkey(snake.go_up,"w")
screen.onkey(snake.go_down,"s")
screen.onkey(snake.go_left,"a")
screen.onkey(snake.go_right,"d")

main()
# update_snake_pose()
screen.mainloop()

