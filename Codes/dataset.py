import cv2
from tkinter import *
from tkinter import messagebox


def login():
    user = name.get()
    code = passs.get()

    if user=="monim" and code=="181311141":
        face_classifier = cv2.CascadeClassifier('F:/Final Project/haarcascade_frontalface_default.xml')

        def face_extractor(img):

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_classifier.detectMultiScale(gray, 1.3, 5)

            if faces is ():
                return None

            for (x, y, w, h) in faces:
                cropped_face = img[y:y + h, x:x + w]

            return cropped_face

        cap = cv2.VideoCapture(0)
        count = 0

        while True:
            ret, frame = cap.read()
            if face_extractor(frame) is not None:
                count += 1
                face = cv2.resize(face_extractor(frame), (200, 200))
                face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

                file_name_path = 'F:/Final Project/dataset/' + str(count) + '.jpg'

                cv2.imwrite(file_name_path, face)

                cv2.putText(face, str(count), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                cv2.imshow('Face Detector', face)
            else:
                pass

            if cv2.waitKey(1) == 13 or count == 50:
                break

        cap.release()
        cv2.destroyAllWindows()
        messagebox.showinfo("Dataset","Sample Collection Complete")
        screen.destroy()

    elif user=="" and code =="":
        messagebox.showerror("Invalid","Username and Password required")

    elif user=="":
        messagebox.showerror("Invalid","Username Required")

    elif code=="":
        messagebox.showerror("Invalid","Password Required")

    elif user!="monim" and code!="181311141":
        messagebox.showerror("Invalid","Please Enter the correct Username and Password")

    elif user!="monim":
        messagebox.showerror("Invalid","Incorrect Username")

    elif code!="181311141":
        messagebox.showerror("Invalid","Incorrect Password")


def back():
    screen.destroy()
    import main


def second_screen():
    global screen
    global name
    global passs

    screen = Tk()
    screen.geometry("650x452+150+80")
    screen.configure(bg="#B2FCFF")
    screen.title("Login")

    lblTitle = Label( text="Please Login", font=("Helvetica", 20, 'bold'), fg="black", bg="#B2FCFF")
    lblTitle.pack(pady=30)

    bordercolor=Frame(screen,bg="black",width=500,height=280)
    bordercolor.pack()

    mainframe=Frame(bordercolor,bg="#74EAEF",width=500,height=280)
    mainframe.pack(padx=20,pady=20)

    Label(mainframe,text="Username : ",font=("Helvetica",18,"bold"),bg="#74EAEF").place(x=80,y=35)
    Label(mainframe, text="Password : ", font=("Helvetica", 18, "bold"), bg="#74EAEF").place(x=80, y=95)
    Label(mainframe, text="Please login with pre-provided username name and password.", font=("arial", 8, "bold"), bg="#74EAEF").place(x=80, y=10)

    name = StringVar()
    passs = StringVar()

    entry_name=Entry(mainframe,textvariable=name,width=15,bd=5,font=("arial",20))
    entry_name.place(x=240,y=35)
    entry_pass=Entry(mainframe,textvariable=passs,width=15,bd=5,font=("arial",20),show="*")
    entry_pass.place(x=240,y=95)

    Button(mainframe,text="Login",height="2",width=20,bg="#ed3833",fg="white",bd=6,command=login).place(x=240,y=170)
    Button(mainframe, text="<<Back<<", height="1", width=10, bg="#74EAEF", fg="Black", bd=4, command=back).place(x=10,
                                                                                                               y=185)


second_screen()

