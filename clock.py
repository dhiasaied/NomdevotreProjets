from tkinter import *
from tkinter.ttk import *
from time import strftime

top = Tk()
top.title("Digital Clock")

def update_time():
    text = strftime('%H:%M:%S %p')
    lbl.config(text=text)
    lbl.after(1000, update_time)

# Customizing the style
style = Style()
style.configure('TLabel', font=('digital-7', 50, 'bold'), background='black', foreground='red')

lbl = Label(top, style='TLabel')
lbl.pack(anchor='center')

update_time()

mainloop()
