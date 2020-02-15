#importing functions
import time
import webbrowser
import random
import datetime
import os
import pyttsx3



print("INITIALIZING EDITH ")
time.sleep(1)
print("OPERATION DONE SUCSESSFULLY")


time.sleep(1)
#voice!
engien = pyttsx3.init()
voices = engien.getProperty('voices')
engien.setProperty('voice',voices[0].id)


#speech!
def say(text):
	engien.say(text)
	engien.runAndWait()
#input
def AI_break():
	print"I AM HERE..."
	while True:
		a1 = raw_input("")
		break
def AI():
	while True:
		a2 = raw_input("")
def AI_none():
	while True:
		a3 = raw_input("")
		break
		

#greetinng
print("GOOD EVENING ")
say("GOOD EVENING ")

print("PLESE GIVE ME YOUR ID")
say("please give me your i d")

AI_none()

if AI_none == "ayan":
	print("WELCOME BACK YOU HAVE MY ACESESS")
	say("WELCOME BACK YOU HAVE MY ACESESS")
print("WHAT CAN I HELP YOU ")
say("WHAT CAN I HELP YOU ")



#input!



	#intelegens 1 random

