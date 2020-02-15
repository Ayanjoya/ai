#import package
import turtle
import time
import webbrowser
import random
import pyttsx3
import getpass
import wikipedia
import smtplib, ssl
import sys
import os
import wolframalpha
import threading
from PIL import Image
from datetime import datetime
from playsound import playsound


im = Image.open(r"/Users/Baran/Documents/sreenshots/jarvisewall.jpg")



#jarvise

#variables
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice' , voices[0].id)

pass_word = "12345"

user_name = "ayan"

#functions
def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def greet():
    time.sleep(1)
    speak("inishlizing jarvis")
    print("INISHLIZING J.A.R.V.I.S.")
    speak("just a second sir")
    print("JUST A SEC SIR...")
    speak("connecting to remote servers")
    print("CONNECTING TO REMOTE SERVERS")
    speak("checking sequrity connections")
    print("CHECKING SEQURITY CONNECTIONS")
    speak("updating drives")
    print("UPDATING ALL THE DRIVES")
    speak("all the drives are updated sucksesfully")
    print("ALL THE DRIVES ARE UPDATED SUCCESFULLY")
    time.sleep(1)
    speak("welcome back sir")
    print("WELCOME BACK SIR...")

def google():
    g = webbrowser.open_new_tab('http://www.google.com')

def youtube():
    y = webbrowser.open_new_tab('http://www.youtube.com/')

def gmail():
    y = webbrowser.open_new_tab('http://www.gmail.com/')

def search():
    speak("what do you want to search on wikipedia page")
    google = input(':')
    gsearch = wikipedia.page(google)
    speak("ok searching on wikipedia")
    print(gsearch.summary)
    speak("according to wikipedia")
    speak(gsearch.summary)


def timeshow():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    speak(current_time)
    print("the current time is ",current_time)

def introduction():
	speak("i think you need my introduction")
	speak("my name is jarvis")
	print("MY NAME IS J.A.R.V.I.S")
	speak("it stands for just  a  rather  very  intelegense  system")
	print("J = JUST")
	print("A = A")
	print("R = RATHER")
	print("V = VERY")
	print("I = INTELEGENT")
	print("S = SYSTEM")
	speak("i was made on 26 jan 2020")

def music():
	playsound('/Users/Baran/Documents/sreenshots/music/come.mp3')

def weather():
	speak("ok showing todays weather forcast")
	w = "weather forecast"
	webbrowser.open_new_tab('http://www.google.com/search?btnG=1&q=%s' % w)

#a loop for input of user
a = getpass.getpass("USER NAME: ")
b = getpass.getpass("PASSWORD: ")


if a == user_name:
    if b == pass_word:
        greet()
        im.show()

else:
    speak("sorry but you dont have my acksess check password and username")
    quit()

while True:
    user = input("")

    if user == "open google" or user == "google":
        speak("opening google")
        google()

    elif user == "open youtube" or user == "youtube":
        speak("opening youtube")
        youtube()

    elif user == "open gmail" or user == "gmail":
        speak("opening gmail")
        gmail()

    elif user == "google search" or user == "search":
        search()

    elif user == "what time is it" or user == "what is the time" or user == "time":
        timeshow()

    if user == "who are you":
        introduction()

    elif user == "play music" or user == "music":
        speak("heres your music sir")
        speak("enjoy")
        music()

    elif user == "stop":
      speak("ok have a good day sir bye")
      quit()

    elif user == "show weather report" or user == "what is weather today" or user == "weather":
        weather()
