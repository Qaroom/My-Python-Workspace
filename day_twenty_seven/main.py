import tkinter

screen=tkinter.Tk()

screen.title("Mile to Km converter :)")
screen.minsize(width=640,height=480)
screen.maxsize(width=640,height=480)
input=tkinter.Entry()
input.config(width=10)
input.grid(column=1,row=0,padx=10,pady=5)

my_label=tkinter.Label(text="Miles")
my_label.grid(column=2,row=0)
my_label.config(padx=10,pady=5)
# my_label.pack(fill=("both"))
# my_label.pack(fill=)
my_label_2=tkinter.Label(text= " is equal ")
my_label_2.grid(column=0,row=1,pady=5,padx=10)
mile_to_km_value=0
my_label_2=tkinter.Label(text= f"{mile_to_km_value}")
my_label_2.grid(column=1,row=1)
my_label_2=tkinter.Label(text= "Km")
my_label_2.grid(column=2,row=1)

def button_clicked():
    number=int(input.get())
    mile_to_km_value=number*1.6
    my_label_2.grid(column=1,row=1)
    my_label_2.config(text=f"{mile_to_km_value}")
    



button=tkinter.Button(text="click me",command=button_clicked)
button.grid(column=1,row=3,padx=0,pady=5)
test=tkinter.Canvas(width=100,height=100)
test.canvasx(50)
test.grid(column=5,row=5)


# input=tkinter.Entry()
# input.config(width=10)
# input.grid(column=200,row=200,padx=4,pady=4)








screen.mainloop()

def add(*args):
    for n in args: 
        print(n)
