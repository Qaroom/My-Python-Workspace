from tkinter import * 
from tkinter import messagebox
from functools import partial
import pandas
import random 

BACKGROUND_COLOR = "#B1DDC6"

data=pandas.read_csv("/home/ros2/Desktop/My-Python-Workspace/day_31/data/french_words.csv")

data_list=data.to_dict(orient="records")
data_list_1=None

def show_cards(img_type="front"):
    global photo_front, photo_back ,title_text, word_text, data_list, data_list_1
    
    try:
        if img_type =="front":
            data_list_1=random.choice(data_list)
            canvas_1.coords(photo_back, 4000, 2603)
            canvas_1.coords(photo_front, 400, 263)
            canvas_1.itemconfig(title_text,text="English",fill="black")
            canvas_1.itemconfig(word_text,text=data_list_1["English"],fill="black")

        elif img_type=="back" : 
            canvas_1.coords(photo_front, 4000, 2603)
            canvas_1.coords(photo_back, 400, 263)
            canvas_1.itemconfig(title_text,text="Turkish",fill="white")
            canvas_1.itemconfig(word_text,text=data_list_1["Turkish"],fill="white")
        else: 
            return    
    except:
        return
    
def screen_close():
    if_sure=messagebox.askyesno(title="Info",message="Do you confirm closing the window?")
    if if_sure:
        screen.destroy()


screen=Tk()
screen.title("Capstone")
screen.config(padx=50,pady=50,background=BACKGROUND_COLOR)

canvas_1=Canvas(width=800,height=526,background=BACKGROUND_COLOR,highlightthickness=0)
canvas_1.grid(column=0,row=0,columnspan=2)


img_back = PhotoImage(file="/home/ros2/Desktop/My-Python-Workspace/day_31/images/card_back.png")
photo_back = canvas_1.create_image(4000, 2603, image=img_back)

img_front = PhotoImage(file="/home/ros2/Desktop/My-Python-Workspace/day_31/images/card_front.png")
photo_front=canvas_1.create_image(4000,2063,image=img_front)


right_image=PhotoImage(file="/home/ros2/Desktop/My-Python-Workspace/day_31/images/right.png")
wrong_image=PhotoImage(file="/home/ros2/Desktop/My-Python-Workspace/day_31/images/wrong.png")


right_button=Button(image=right_image,command=partial(show_cards,img_type="front"),highlightthickness=0)
right_button.grid(column=1,row=1,pady=20)

back_button=Button(image=wrong_image,command=partial(show_cards,img_type="back"),highlightthickness=0,)
back_button.grid(column=0,row=1,pady=20)

title_text=canvas_1.create_text(400, 150,text="",font=("Arial",40,"italic"))
word_text=canvas_1.create_text(400, 263,text="",font=("Arial",60,"bold"))

screen.protocol("WM_DELETE_WINDOW",screen_close)
show_cards()
screen.mainloop()