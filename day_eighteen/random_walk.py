from turtle import Turtle , Screen ,colormode
import random

distance=100
kom=Turtle()
kom.shape("turtle")
colormode(255)

# kom.pensize(10)

random_angule=[0,90,180,270]
def random_walk():
    kom.forward(distance)
    kom.setheading(random.choice(random_angule))
    # # if x == 0:
    # #     kom.forward(distance)
    # # else:
    # #     kom.backward(distance)
    # if y == 0: 
    #     kom.right(90)
    # else : kom.left(90)



def draw_spirograph(angule):
    kom.speed(1000)
    for _ in range(round(360/angule)):
        color_r=random.randint(0,255)
        color_g=random.randint(0,255)
        color_b=random.randint(0,255)
        kom.pencolor(color_r,color_g,color_b)
        kom.circle(100)
        kom.setheading(kom.heading()+angule)
draw_spirograph(0.5)


screen=Screen()
screen.exitonclick()
# for _ in range(1):
#     color_r=random.randint(0,255)
#     color_g=random.randint(0,255)
#     color_b=random.randint(0,255)
#     kom.speed(11)
#     kom.pencolor(color_r,color_g,color_b)
#     # x=random.randint(0,1)
#     # y=random.randint(0,1)
#     # random_walk()

    

