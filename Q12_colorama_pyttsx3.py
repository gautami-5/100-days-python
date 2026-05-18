import colorama
 #External Module for colored text in terminal
print(colorama.Fore.GREEN + "Hey! This is Gautami")

import pyttsx3
#External Module for text to speech
engine = pyttsx3.init()
engine.say("Hey Gautami")
engine.runAndWait()