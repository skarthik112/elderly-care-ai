# utils/voice_alert.py
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 170)  # Adjust speed
    engine.say(text)
    engine.runAndWait()
