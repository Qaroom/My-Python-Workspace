from turtle import Turtle , Screen ,colormode
import random

distance=100
kom=Turtle()
kom.shape("turtle")
colormode(255)

# kom.forward(distance)
# kom.right(90)
# kom.forward(distance)
# kom.right(90)
# kom.forward(distance)
# kom.right(90)
# kom.forward(distance)
# kom.right(90)
# kom.goto(100.0,100.0)
# kom.sety(50)
# kom.circle(50)
# kom.fillcolor(2,2,2)
# for _ in range(10):
#     kom.pencolor(2,2,2)
#     kom.forward(distance) 
#     kom.penup()
#     kom.forward(distance) 
#     kom.pendown()
def turtle_draw(side_number):
    angule=360/side_number
    for _ in range(side_number):
        kom.forward(distance)
        kom.right(angule) 


for side in range(3,10):
    color_r=random.randint(0,255)
    color_g=random.randint(0,255)
    color_b=random.randint(0,255)
    kom.pencolor(color_r,color_g,color_b)
    turtle_draw(side)


    
screen=Screen()
screen.exitonclick()