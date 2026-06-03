from turtle import Screen
from car_class import CarObject
from obstacles_class import Obstacles
from scoreboard import ScoreBoard
scoreboard=ScoreBoard()
screen=Screen()
screen.tracer(0)
screen.setup(width=800,height=800)
screen.bgcolor("white")
screen.title("Crossing Capstone")
car=CarObject()
obstacles=Obstacles()


def main():
    screen.update()
    obstacles.move_obstacles()

    if car.ycor()>=380:
        car.go_to_starting_posetion()
        obstacles.add_obstacles()
        scoreboard.score+=1
        scoreboard.update_score()

    if scoreboard.score==10:
        scoreboard.winner()

    if scoreboard.life_number ==0:
        scoreboard.game_over()
        obstacles.is_game_on=False
        

    if obstacles.check_accidents(car.position()): 
        scoreboard.life_number-=1
        car.go_to_starting_posetion()
        scoreboard.update_score()
    



    screen.ontimer(main,50)


main()
screen.listen()
screen.onkeypress(car.move_up,"w")
screen.onkeypress(car.move_down,"s")
screen.onkeypress(car.move_right,"d")
screen.onkeypress(car.move_left,"a")
screen.mainloop()