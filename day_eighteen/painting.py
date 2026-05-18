from turtle import Turtle , Screen ,colormode
import random
import colorgram

color_list=colorgram.extract("My-Python-Workspace\day_eighteen\spot_painting.jpg",20)
print(type(color_list))
distance=75
kom=Turtle()
kom.shape("turtle")
print(kom.screen.screensize())
colormode(255)
# print(color_list)
# kom.pencolor(random.choice(color_list).rgb)
kom.pensize(10)
# kom.dot()
# kom.penup()
# kom.forward(distance)
# kom.dot()
# kom.forward(distance)
# kom.dot()
# kom.forward(distance)


# kom.setx(0)
# kom.sety(kom.ycor()+100)
kom.penup()
kom.sety(-370)
for _ in range(11):
    kom.setx(-370)

    for _ in range(11):
        kom.pencolor(random.choice(color_list).rgb)
        kom.dot()
        kom.forward(distance)

    kom.sety(kom.ycor()+distance)

def draw_spirograph(angule):
    kom.speed(1000)
    for _ in range(round(360/angule)):
        color_r=random.randint(0,255)
        color_g=random.randint(0,255)
        color_b=random.randint(0,255)
        kom.pencolor(color_r,color_g,color_b)
        kom.circle(100)
        kom.setheading(kom.heading()+angule)
# draw_spirograph(0.5)


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

    

