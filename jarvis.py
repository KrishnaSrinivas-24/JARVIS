import speech_recognition as sr
import pyttsx3
import datetime
import os
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that. Could you repeat?")
            return listen()

def greet():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good morning! Allow me to introduce myself I am Jarvis, the virtual artificial intelligence and I'm here to assist you with a variety of tasks as best I can, 24 hours a day seven days a week.")
    elif 12 <= hour < 18:
        speak("Good afternoon! Allow me to introduce myself I am Jarvis, the virtual artificial intelligence and I'm here to assist you with a variety of tasks as best I can, 24 hours a day seven days a week.")
    else:
        speak("Good evening! Allow me to introduce myself I am Jarvis, the virtual artificial intelligence and I'm here to assist you with a variety of tasks as best I can, 24 hours a day seven days a week.")

greet()

def execute_command(command):
    if "open google" in command:
        open_google()
    elif "open youtube" in command:
        open_youtube()
    elif "open edge" in command:
        open_Edge()

    # Add more commands here as you like this
def open_google():
    speak("Opening Google")
    os.system("start chrome")

def open_Edge():
    speak("Opening Edge")
    os.system("start msedge")

def open_youtube():
    speak("Opening Youtube")
    os.system("start chrome https://www.youtube.com/")

while True:
    command = listen()
    if "exit" in command:
        break
    else:
        execute_command(command)
