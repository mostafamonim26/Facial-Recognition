import tkinter as tk
from PIL import Image,ImageTk
import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import os



root = tk.Tk()
root.title('Face Recognition by Mostafa Monim')

canvas = tk.Canvas(root, width=590, height=390)
canvas.grid(columnspan=3, rowspan=4)

bg = Image.open('F:/Final Project/bgimg22.jpg')
bg = ImageTk.PhotoImage(bg)
canvas.create_image(0,0, image=bg, anchor= "nw")
canvas.create_text(300, 50, text="Facial-Recognition System", font=("Helvetica", 25), fill= "white")
canvas.create_text(150, 100, text="* We can add any type of application here.", font=("arial", 12), fill= "yellow")
canvas.create_text(251, 120, text="* This program will provide security for the program instead of this page.", font=("Helvetica", 12), fill= "yellow")
canvas.create_text(182, 140, text="* Only the identified user can access to the program", font=("Helvetica", 12), fill= "yellow")
canvas.create_text(179, 160, text="* For example I added the Virtual Assistant System", font=("arial", 12), fill= "yellow")
canvas.create_text(166, 180, text="* Click on <Virtual Assistant> button to execute.", font=("arial", 12), fill= "yellow")
canvas.create_text(222, 200, text="* Click on <Example2> button to see another example program.", font=("arial", 12), fill= "yellow")

#functions
def exit():
    root.destroy()
    exit

def example():
    root.destroy()
    import example2


def open_file2():
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

    def speak(audio):
        engine.say(audio)
        engine.runAndWait()

    def wishMe():
        hour = int(datetime.datetime.now().hour)
        if hour >= 0 and hour < 12:
            speak("Good Morning!")

        elif hour >= 12 and hour < 18:
            speak("Good Afternoon!")

        else:
            speak("Good Evening!")

        speak("I am your virtual assistant.... How can i help you")

    def takeCommand():
        # It takes microphone input from the user and returns string output

        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")

        except Exception as e:
            # print(e)
            print("Say that again please...")
            return "None"
        return query




    if __name__ == "__main__":
        wishMe()
        while True:
            if 1:
                query = takeCommand().lower()

            # Logic for executing tasks based on query

            if 'open youtube' in query:
                webbrowser.open("youtube.com")

            elif 'open google' in query:
                speak("Opening google")
                webbrowser.open("google.com")

            elif 'open stackoverflow' in query:
                webbrowser.open("stackoverflow.com")

            elif 'you can go now' in query:
                speak("Thank you sir. See you later.")
                exit()


            elif 'play music' in query:
                music_dir = 'F:\\Amear Acha Juall'
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir, songs[0]))

            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is {strTime}")


            elif 'open code' in query:
                codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)



#button
button1_text = tk.StringVar()
button1 = tk.Button(root, textvariable=button1_text,bd=6, command=lambda:exit(), font="Raleway", bg="#FF5555", fg="black", height=2, width=10)
button1_text.set("Exit")
button1.grid(column=2, row=3)

button2_text = tk.StringVar()
button2 = tk.Button(root, textvariable=button2_text,bd=6, command=lambda:open_file2(), font="Raleway", bg="#20bebe", fg="black", height=2, width=14)
button2_text.set("Virtual Assistant")
button2.grid(column=0, row=3)

button3_text = tk.StringVar()
button3 = tk.Button(root, textvariable=button3_text,bd=6, command=lambda:example(), font="Raleway", bg="#20bebe", fg="black", height=2, width=10)
button3_text.set("Example2")
button3.grid(column=1, row=3)


root.mainloop()
