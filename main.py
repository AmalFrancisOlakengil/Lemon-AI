import speech_recognition as sr
from gtts import gTTS
import os
import webbrowser
from tkinter import *
import sqlite3

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
    
def start_listening():
    app_name = listen()
    open_application(app_name)

window = Tk()
window.geometry("600x400")
window.title("Voice Command App")

listen_button = Button(window, text="Start Listening", command=start_listening)
listen_button.pack(pady=20)

window.mainloop()


