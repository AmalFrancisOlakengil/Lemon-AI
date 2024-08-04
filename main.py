#imports
from re import T
from tkinter.font import BOLD
import speech_recognition as sr
from gtts import gTTS
import os
import webbrowser
from tkinter import *
import sqlite3
from tkinter import ttk


# audio recognition
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text.lower()
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return ""
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return ""

# app access
def open_application(app_name):
    if app_name == "open opera":
        os.startfile(r"C:\Users\franc\AppData\Local\Programs\Opera\opera.exe") 
    elif app_name == "open visual studio code":
        os.startfile(r"C:\Users\franc\AppData\Local\Programs\Microsoft VS Code\Code.exe") 
    elif app_name == "open edge":
        os.startfile(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe") 
    elif app_name == "open youtube":
        webbrowser.open("https://www.youtube.com/")
    elif app_name == "open github":
        webbrowser.open("https://github.com/")
    elif app_name == "open chat gpt":
        webbrowser.open("https://chatgpt.com/")
    else:
        print("Application not recognized")
  
# entry function
def start_listening():
    app_name = listen()
    open_application(app_name)

# window set up
window = Tk()
window.geometry("450x400")
window.minsize(width="450",height="400")
window.maxsize(width="450",height="400")
window.title("Voice Command App")

#tab creation
notebook = ttk.Notebook(window)
tab1 = Frame(notebook)
tab2 = Frame(notebook)
tab3 = Frame(notebook)
notebook.add(tab1, text="Assistant")
notebook.add(tab2, text="Add New")
notebook.add(tab3, text="Speech To Text")
notebook.pack(expand=True, fill = "both")
tab1.configure(background="white")
tab2.configure(background="white")
tab3.configure(background="white")

#tab 1
listen_button = Button(tab1, text="START LISTENING", command=start_listening,bg = "black", fg = "white", font = ('Arial', 10, BOLD))
listen_button.pack(expand=True)

#tab2
TAN = Label(tab2, text="ENTER APPLICATION NAME", font = ('Helvetica', 10, BOLD), bg = "white").pack(expand=True)
add_new = Entry(tab2).pack(expand=True)
TANA =  Label(tab2, text="ENTER APPLICATION ADDRESS", font = ('Helvetica', 10, BOLD),bg = "white").pack(expand=True)
new_address = Entry(tab2).pack(expand=True)

#tab3

window.mainloop()


