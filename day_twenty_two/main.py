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
computer_wall.move_walls_down()
computer_wall.move_walls_down()
pong_ball.move_pong_ball("CCW")
pong_ball.second_heading_value=45
def main():
    screen.update()
    
    pong_ball.move_pong_ball("")
    check_user_parametre=user_wall.check_distance(pong_ball.update_pose_of_pong())
    check_computer_parametre=computer_wall.check_distance(pong_ball.update_pose_of_pong())
    pong_ball.check_pose_of_pong(user_state=check_user_parametre,
                                 computer_state=check_computer_parametre)
    computer_wall.move_wall_auto(pong_ball.update_pose_of_pong())
    # user_wall.move_wall_auto(pong_ball.update_pose_of_pong())

    if check_user_parametre:
        score_of_pong.user_score+=1
        score_of_pong.update_score()
    elif  check_computer_parametre:
        score_of_pong.computer_score+=1
        score_of_pong.update_score()
    screen.ontimer(main,50)

    if pong_ball.update_pose_of_pong()[0] >=600:
        score_of_pong.game_over()


main()
# pong_ball.move_pong_ball("CW")
# pong_ball.move_pong_ball("CW")
# pong_ball.move_pong_ball("CW")
screen.listen()
screen.onkeypress(user_wall.move_walls_up,"w")
screen.onkeypress(user_wall.move_walls_down,"s")
screen.mainloop()
