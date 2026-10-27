# 3. Install an external module and use it to perform an operation of your interest.

import pyttsx3

# pyttsx3.speak("Hello World")
engine = pyttsx3.init()
says = input("Enter what do you want to say: ")
engine.say(says)
engine.runAndWait()