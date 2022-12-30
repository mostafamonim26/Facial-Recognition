import tkinter as tk
from PIL import Image,ImageTk
root = tk.Tk()
root.title('Facial-Recognition by Mostafa Monim')

canvas = tk.Canvas(root, width=590, height=390)
canvas.grid(columnspan=3, rowspan=4)

bg = Image.open('F:/Final Project/bgimg22.jpg')
bg = ImageTk.PhotoImage(bg)
canvas.create_image(0,0, image=bg, anchor= "nw")

canvas.create_text(300, 50, text="Facial-Recognition System", font=("Helvetica", 25), fill= "white")
canvas.create_text(150, 150, text="* Welcome to facial recognition system.", font=("arial", 12), fill= "yellow")
canvas.create_text(200, 170, text="* At first user have to set sample picture to the dataset.", font=("Helvetica", 12), fill= "yellow")
canvas.create_text(244, 190, text="* By clicking <Take Images> user can set his/her face for detection.", font=("Helvetica", 12), fill= "yellow")
canvas.create_text(181, 210, text="* For this user have to login with provided details.", font=("arial", 12), fill= "yellow")
canvas.create_text(198, 230, text="* Click on <Facial Recognition> for user identification.", font=("arial", 12), fill= "yellow")

#functions
def open_file():
    root.destroy()
    import detaction



def open_file1():
    root.destroy()
    import dataset



#button
button1_text = tk.StringVar()
button1 = tk.Button(root, textvariable=button1_text,bd=6, command=lambda:open_file(), font="Raleway", bg="#06D3DB", fg="black", height=2, width=15)
button1_text.set("Facial Recognition")
button1.grid(column=2, row=3)

button2_text = tk.StringVar()
button2 = tk.Button(root, textvariable=button2_text,bd=6, command=lambda:open_file1(), font="Raleway", bg="#06D3DB", fg="black", height=2, width=15)
button2_text.set("Take Images")
button2.grid(column=0, row=3)


root.mainloop()

