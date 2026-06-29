from tkinter import *
import math
from functools import partial
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
second_value=25*60


window=Tk()
window.title("Pomodoro")
window.minsize(200,224)
window.config(background=YELLOW,padx=100,pady=120)

def counter():
    global second_value
    min_count=math.floor(second_value/60)
    sec_count=second_value%60
    if sec_count<10:
        sec_count=f"0{sec_count}"

    if min_count<10:
        min_count=f"0{min_count}"

    canvas.itemconfig(clock_text,text=f"{min_count}:{sec_count}")
    if second_value >0:
        second_value-=1
        window.after(1000,counter)


def reset_counter():
    global second_value
    second_value=25*60

label_1=Label(text="Timer",font=(FONT_NAME,50,"bold"),background=YELLOW,highlightthickness=0,fg=GREEN)
label_1.grid(column=1,row=0)

start_button=Button(text="Start",background=GREEN,fg="white",font=(FONT_NAME,12,"bold")
                    ,highlightthickness=0,command=counter)
start_button.grid(column=0,row=2)

reset_button=Button(text="Reset",background=GREEN,fg="white",font=(FONT_NAME,12,"bold")
                    ,highlightthickness=0,command=reset_counter)
reset_button.grid(column=2,row=2)

label_2=Label(text="✔",font=(FONT_NAME,20,"bold"),background=YELLOW,highlightthickness=0,fg=GREEN)
label_2.grid(column=1,row=2)

canvas=Canvas(width=200,height=224,background=YELLOW,highlightthickness=0)

tomoto_image=PhotoImage(file="/home/ros2/Desktop/My-Python-Workspace/day_28/tomato.png")
canvas.create_image(100, 112, image=tomoto_image)
canvas.grid(column=1,row=1,padx=50,pady=50)
clock_text=canvas.create_text(100,128,text="00:00",font=(FONT_NAME,30,"bold"),fill="white")
# canvas.pack()

# counter(25*60)

window.mainloop()