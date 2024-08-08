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

#sql connect
conn = sqlite3.connect('Path.db')
c = conn.cursor()
c.execute("""
CREATE TABLE IF NOT EXISTS my_table (
    App text,
    path text
);
""")

# sql storage
def app_path():
    App_name = add_new.get()
    App_path = new_address.get()
    c.execute("INSERT INTO my_table (App, path) VALUES (?, ?)", (App_name, App_path))
    conn.commit()
    
# audio recognition
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
      
        
        # Set timeout and phrase time limit
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            try:
                text = recognizer.recognize_google(audio)
             
                return text.lower()
            except sr.UnknownValueError:
                
                return ""
            except sr.RequestError as e:
              
                return ""
        except sr.WaitTimeoutError:
          
            return ""

# app access
def open_application(app_name):
       c.execute("SELECT * FROM my_table")
       data = c.fetchall()
       for item in data:
           if app_name == "open " + item[0]:
               if "exe" in item[1]:
                    os.startfile(item[1]) 
               elif "com" in item[1]:
                  webbrowser.open(item[1])
               else:
                   pass
                   
# entry function
def start_listening():
    app_name = listen()
    open_application(app_name)

#Tab 3 entry
def start_listening2():
    txt = listen()
    STT.insert(END, txt+"\n")

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
logo = PhotoImage(file="C:\\Users\\franc\\source\\repos\\Lemon AI\\R.png")
icon = Label(tab1, image=logo, borderwidth=0, bg = "white").pack(pady = 50)
listen_button = Button(tab1, text="START LISTENING", command=start_listening,bg = "black", fg = "white", font = ('Arial', 10, BOLD))
listen_button.pack(expand=True)
display = "Speak clearly"
Status = Label(tab1, text = display, font = ('Helvetica', 10, BOLD), bg = "white").pack(expand=True)

#tab 2
TAN = Label(tab2, text="ENTER APPLICATION NAME", font = ('Helvetica', 10, BOLD), bg = "white").pack(expand=True)
add_new = Entry(tab2)
add_new.pack(expand=True)
TANA =  Label(tab2, text="ENTER APPLICATION ADDRESS", font = ('Helvetica', 10, BOLD),bg = "white").pack(expand=True)
new_address = Entry(tab2)
new_address.pack(expand=True)
submit_button = Button(tab2, text = "SUBMIT", command = app_path, bg = "black", fg = "white",font = ('Arial', 10, BOLD))
submit_button.pack(expand=True)

#tab 3
STT = Text(tab3, relief=SOLID, font=('Arial', 10, 'bold'), height=20)
STT.pack(side="top")
listen_button3 = Button(tab3, text="START LISTENING", command=start_listening2,bg = "black", fg = "white", font = ('Arial', 10, BOLD))
listen_button3.pack(side="bottom")

window.mainloop()
