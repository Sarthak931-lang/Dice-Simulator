from tkinter import *
import random
def rolldice():
    numbers=["\u2680","\u2681","\u2682","\u2683","\u2684","\u2685"]
    label.configure(text=f"{random.choice(numbers)}")
    label.pack()
tk=Tk()
tk.title("Dice Simulator")
tk.geometry("400x500")
button=Button(tk,font=("Helvitica",25,"bold"),text="Dice Roll",command=rolldice,bg="lightblue",fg="red")
button.pack()
label=Label(tk,font=("Helvitica",300,"bold"),text="",fg="green")
label.pack()
tk.mainloop()
