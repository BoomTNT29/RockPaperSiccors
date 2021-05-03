from tkinter import *
import center_tk_window
from tkinter import messagebox

def main():
    root = Tk()
    root.title("GJ Industries")
    w = 290
    h = 640
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws/2) - (w/2)    
    y = (hs/2) - (h/2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    heading = Label(root, text='RPS', font=("calibri", 20, "bold"))
    heading.pack()
    
    multiplayer_button = Button(root, text="multiplayer", command= , width=15, height=5, font("calibri", 13, "bold"))