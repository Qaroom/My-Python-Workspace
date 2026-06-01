from turtle import  Screen ,Turtle
from wall_calss import WallClass
from pong_ball import PongBall
screen=Screen()
screen.setup(width=1200,height=600)
screen.bgcolor("black")


screen.title("My Snake Game")
screen.update()
screen.tracer(0)

user_wall=WallClass()
computer_wall=WallClass()
pong_ball=PongBall()
computer_wall.set_wall_pose_to_another_side()


def main():
    screen.update()
    pong_ball.move_pong_ball()
    

    screen.ontimer(main,50)


main()

screen.listen()
screen.onkeypress(user_wall.move_walls_up,"w")
screen.onkeypress(user_wall.move_walls_down,"s")
screen.mainloop()
