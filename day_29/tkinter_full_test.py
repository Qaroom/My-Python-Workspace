from tkinter import *
from tkinter import messagebox
import json
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

last_x, last_y = None, None

circle=None
def start_draw(event):
    global last_x, last_y , circle
    if event.num==1:

        last_x , last_y= event.x , event.y
    elif event.num==3:
        last_x , last_y= event.x , event.y
        circle=canvas_1.create_oval(last_x,last_y,event.x,event.y,width=2)
    

def draw(event):
    global last_x, last_y
    
    canvas_1.create_line(last_x,last_y,event.x,event.y,smooth=True,width=2,fill=GREEN)
    last_x , last_y= event.x , event.y
    
def draw_circle(event):
    global last_y, last_x,circle
    canvas_1.coords(circle, last_x, last_y, event.x, event.y)
    
def clear_canvas(event):
    global circle
    if_ok=messagebox.askokcancel("Uyari","Icerik silinmesinden emin misiniz?")
    if if_ok:
        last_x , last_y= event.x , event.y
    else : 
        return
    # print(canvas_1.find_withtag(circle))

    canvas_1.delete("all")

def reset(event): 
    global last_y, last_x
    last_x , last_y= None, None

def close_screen(c):
    screen.destroy()

def print_info():
    print(text.get())
    text.delete(0,"end")
screen=Tk()
screen.config(width=640,height=480,background="white",highlightthickness=0)
screen.minsize(width=640,height=480)
screen.title("Full Test Screen")

canvas_1=Canvas(screen,width=320,height=240, background=YELLOW,highlightthickness=0)
canvas_1.grid(column=0,row=0,padx=20,pady=20,columnspan=3,rowspan=3)
text=Entry()
text.config(width=12,bg=GREEN ,highlightthickness=2,highlightcolor=YELLOW)
text.insert(0,"Type any thing")
text.focus()
text.grid(column=3,row=0,columnspan=3 )
get_info=Button()
get_info.config(text="Save",background=PINK,highlightthickness=2,command=print_info)
get_info.grid(column=3,row=1)
new_dic={"key":"value"}
with open("jsondata.json","w") as data_file:
    json.dump(new_dic,data_file,indent=4)

with open("jsondata.json","r") as data_file:

    data=json.load(data_file)
    print(data)

screen.bind("<Button-1>", start_draw)
screen.bind("<B1-Motion>", draw)
screen.bind("<ButtonRelease-1>", reset)
screen.bind("<Button-3>", start_draw)
screen.bind("<B3-Motion>",draw_circle)
screen.bind("<ButtonRelease-3>", reset)
screen.bind("<Button-2>",clear_canvas)
screen.bind("c",close_screen)


screen.focus_set()
screen.mainloop()