from turtle import  Screen
from wall_calss import WallClass
from pong_ball import PongBall
from pong_board_score import Pong_Score
screen=Screen()
screen.setup(width=1200,height=600)
screen.bgcolor("black")


screen.title("My Pong Game")
screen.update()
screen.tracer(0)

user_wall=WallClass()
computer_wall=WallClass()
pong_ball=PongBall()
score_of_pong=Pong_Score()

computer_wall.set_wall_pose_to_another_side()
game_speed=50
def main():
    global game_speed
    screen.update()
    pong_ball.move_pong_ball()
    computer_wall.move_wall_auto(pong_ball.update_pose_of_pong())
    if pong_ball.ycor()>=280 or pong_ball.ycor() <=-280:
        pong_ball.bounce_y()
    
    if user_wall.check_distance(pong_ball.update_pose_of_pong()) or computer_wall.check_distance(pong_ball.update_pose_of_pong()) :
        pong_ball.bounce_x()
        game_speed = int(game_speed*0.9)
    
    if pong_ball.xcor() >=590:
        game_speed=50
        pong_ball.goto(0,0)
        score_of_pong.computer_score+=1
        pong_ball.reset_pong_posetion()
        score_of_pong.update_score()

    screen.ontimer(main,game_speed)

main()
screen.listen()
screen.onkeypress(user_wall.move_walls_up,"w")
screen.onkeypress(user_wall.move_walls_down,"s")
screen.mainloop()
