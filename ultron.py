#import package
import turtle
import pyttsx3
import time
import webbrowser
import random
import getpass
import wikipedia
import smtplib, ssl
import os
import speech_recognition as sr
import wolframalpha
import ultron_cal
import threading
import pygame
from PIL import Image
from datetime import datetime
from playsound import playsound


im = Image.open('/Users/Baran/Documents/sreenshots/ulton.jpg')

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice' , voices[7].id)

def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def take_command1():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:

        text = r.recognize_google(audio)
        print(format(text))
        return text
    except:
        print("i cant hear you sir")

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print(format(text))
        return text
    except:
        pass


#functions
def greet():
    print("INISHLIZING ULTRON...")
    speak("inishlizing ultron")
    print("CONNECTING TO REMOTE SERVERS")
    speak("connecting to remote servers")
    print("ACTIVATING SERVER DRIVES")
    speak("activating server drives")
    print("ACTIVATING ULTRON ACSESS")
    speak("activating ultron aksess")
    print("NOW I AM ONLINE!")
    speak("now i am online")
    print("GOOD EVENING BOSS")
    speak("good evening boss")
    im.show()

def search():

    gs = wikipedia.page(query)
    print(gs.summary)
    speak("according to wikipedia")
    speak(gs.summary)

def music():
    speak("playin your music boss")
    

    pygame.mixer.init()
    pygame.mixer.music.load('/Users/Baran/Documents/sreenshots/music/come.mp3')
    pygame.mixer.music.set_volume(100)
    pygame.mixer.music.play(-1)
def weather():
    speak("showing todays weather forcast")
    we = webbrowser.open_new_tab('http://www.google.com/search?btnG=1&q=weather forecast')

def web():
    speak("which website")
    query0 = take_command1()
    op = webbrowser.open_new_tab('http://www.google.com/search?btnG=1&q=%s'% query0 )


def times():
    t = webbrowser.open_new_tab('http://www.google.com/search?btnG=1&q=time')
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    speak(current_time)
    print("the current time is ",current_time)

    return
def maths():
    ultron_cal.start()

def stopm():
    pygame.mixer.music.stop()


print("SPEAK YOUR PASSWORD!")
query1 = take_command1()
if 'password' in query1:
    speak("the password is karrect")
    speak("just a minute")
    greet()
else:
    speak("the password is incarrect")
    quit()

while True:
    query = take_command()

    try:

        if 'search' in query:
            search()

        elif 'music' in query:
            music()

        elif 'weather' in query:
            weather()

        elif 'time' in query:
            times()

        elif 'website' in query:
            web()

        elif 'maths' in query:
            maths()

        elif 'sleep' in query:
            speak("have a good day boss")
            quit()

        elif 'stop' in query:
            stopm()
    except TypeError:
        pass
