from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
#import text_to_speech as speech
import speech_recognition as s
import threading
#import pyaudio
import pyttsx3 as p


engine = p.init()

voices = engine.getProperty('voices')
print(voices)

engine.setProperty('voice', voices[1].id)


def speak_bot(word):
     engine.say(word)
     engine.runAndWait()

chatbot = ChatBot(" MY CHATBOT")
convers = ["Hi",
           "Hello, thanks for visiting",
            "How are you",
           "Good to see you again",
            "Is anyone there?",
            "Hi there, how can I help?",
            "Hello", "Good day",
           "Bye",

          "See you later",
           "Thanks", "Thank you",
           "Goodbye",
           "That's helpful",
         "See you later",
            "Happy to help!",
          "Have a nice day",
             "Any time!",
          "Bye! Come back again soon.",
           "My pleasure",
   
         "What hours are you open?",
          "What are your hours?",
          "When are you open?" ,
          "We're open every day 9am-9pm",
           "Our hours are 9am-9pm every day",
       
          "Do you take credit cards?",
           "Do you accept Mastercard?",
           "Are you cash only?" ,
        "We accept VISA, Mastercard and AMEX",
         "We accept most major credit cards",
     
        "Are you open today?",
         "When do you open today?",
         "What are your hours today?",
       "We're open every day from 9am-9pm",
        "Our hours are 9am-9pm every day"

]

trainer = ListTrainer(chatbot)

trainer.train(convers)

def speech_reg():
    spr =s.Recognizer()
    spr.pause_threshold =0.8
    print('listening you .........................')
    with s.Microphone() as m:
        try:
            audio=spr.listen(m)
            query= spr.recognize_google(audio)
            print(query)
     
            text.delete(0,END)
            text.insert(0,query)
            button_clicked()
        except:
            print('not reconizer')


def button_clicked():
    query = text.get()
    
    bot_ans= chatbot.get_response(query)
    mess.insert(END, 'you:' +query)
    mess.insert(END,'Bot:'+str(bot_ans))
    speak_bot(bot_ans)
    text.delete(0,END)
    mess.yview(END)
 
win = Tk()

win.geometry('400x650')
win.title('chatbot')
win.iconbitmap(r'bot.ico')

photo = PhotoImage(file = 'chatbot2.png')
photolable = Label(win,image = photo)
photolable.pack(pady=10)
label=Label(win,text='Talk to me')
label.pack()

frame = Frame(win)
scrol = Scrollbar(frame)
mess= Listbox(frame ,width =60,height=15,yscrollcommand =scrol.set)

scrol.pack(side = RIGHT, fill= Y,)
mess.pack(side = LEFT, fill = X, pady = 15)
frame.pack()

photo1 = PhotoImage(file = 'send.png')
text=Entry(win,font =('italic',15))
text.pack(fill =X,pady=20)
button = Button(win,image = photo1,command = button_clicked)
button.pack()



def enter_function(event):
    button.invoke()

win.bind('<Return>',enter_function)

def repeat():
    while True:
        speech_reg()

t=threading.Thread(target=repeat)

t.start()

win.mainloop()
