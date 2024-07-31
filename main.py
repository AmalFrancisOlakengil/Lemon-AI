import speech_recognition as sr
from gtts import gTTS
import os
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
def open_application(a):
     if a == "open opera":
            os.startfile(r"C:\Users\franc\AppData\Local\Programs\Opera\opera.exe") 
     elif a == "open visual studio code":
            os.startfile(r"C:\Users\franc\AppData\Local\Programs\Microsoft VS Code\Code.exe") 

app_name = listen()
open_application(str(app_name))
