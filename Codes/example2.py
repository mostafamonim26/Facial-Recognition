import tkinter as tk
from PIL import Image,ImageTk
root = tk.Tk()
root.title('Example program')

canvas = tk.Canvas(root, width=590, height=390)
canvas.grid(columnspan=3, rowspan=4)

bg = Image.open('F:/Final Project/bgimg1.jpg')
bg = ImageTk.PhotoImage(bg)
canvas.create_image(0,0, image=bg, anchor= "nw")

def exit():
    root.destroy()

canvas.create_text(300, 50, text="Unlocked Program(example)", font=("Helvetica", 25), fill= "black")
canvas.create_text(129, 150, text="* This is a example window.", font=("arial", 15), fill= "black")
canvas.create_text(264, 170, text="* Here can be any kind of program instead of this example.", font=("arial", 15), fill= "black")
canvas.create_text(240, 190, text="* Which is secured by the Facial Recognition System.", font=("arial", 15), fill= "black")
canvas.create_text(233, 210, text="* Only the specific user can access to this program.", font=("arial", 15), fill= "black")
canvas.create_text(176, 230, text="* Click on <Exit> to close the program.", font=("arial", 15), fill= "black")

button1_text = tk.StringVar()
button1 = tk.Button(root, textvariable=button1_text,bd=6, command=lambda:exit(), font="Raleway", bg="#FF5555", fg="white", height=1, width=8)
button1_text.set("Exit")
button1.grid(column=2, row=3)

root.mainloop()