"""
Text to speech
"""

import cowsay
import pyttsx3


this = input("What's this? ")
cowsay.cow(this)
engine = pyttsx3.init()
engine.say(this)
engine.runAndWait()
