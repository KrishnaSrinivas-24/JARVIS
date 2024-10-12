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

def open_google():
    speak("Opening Google")
    os.system("start chrome")

def open_edge():
    speak("Opening Edge")
    os.system("start msedge")

def open_youtube():
    speak("Opening Youtube")
    os.system("start chrome https://www.youtube.com/")

def open_spotify():
    speak("Opening Spotify")
    os.system("start spotify")

def open_word():
    speak("Opening Word")
    os.system("start winword")  # Correct for Microsoft Word

def open_powerpoint():
    speak("Opening Power point")
    os.system("start powerpnt") # Correct for Microsoft Power Point

def open_excel():
    speak("Opening Excel")
    os.system("start excel")  # Correct for Microsoft excel

def open_calculator():
    speak("Opening Calculator")
    os.system("start calc")

def open_notepad():
    speak("Opening Notepad")
    os.system("start notepad")  # Correct for Notepad

def open_github():
    speak("Opening Github")
    os.system("start chrome https://github.com/")

def open_discord():
    speak("Opening Discord")
    os.system("start chrome https://discord.com/")

def open_command_prompt():
    speak("Opening Command Prompt")
    os.system("start cmd")

def open_file_explorer():
    speak("Opening File Explorer")
    os.system("start explorer")

def execute_command(command):
    if "open google" in command.lower():
        print("Executing command to open Google.")
        open_google()
    elif "open edge" in command.lower():
        print("Executing command to open Edge.")
        open_edge()
    elif "open spotify" in command.lower():
        print("Executing command to open Spotify.")
        open_spotify()
    elif "open youtube" in command.lower():
        print("Executing command to open Youtube.")
        open_youtube()
    elif "open word" in command.lower():
        print("Executing command to open Word.")
        open_word()
    elif "open discord" in command.lower():
        print("Executing command to open Discord.")
        open_discord()
    elif "open notepad" in command.lower():
        print("Executing command to open Notepad.")
        open_notepad()
    elif "open powerpoint" in command.lower():
        print("Executing command to open powerpoint.")
        open_powerpoint()
    elif "open excel" in command.lower():
        print("Executing command to open Excel.")
        open_excel()
    elif "open calculator" in command.lower():
        print("Executing command to open Calculator.")
        open_calculator()
    elif "open command prompt" in command.lower():
        print("Executing command to open Command Prompt.")
        open_command_prompt()
    elif "open file explorer" in command.lower():
        print("Executing command to open File Explorer.")
        open_file_explorer()
    elif "open github" in command.lower():
        print("Executing command to open Github.")
        open_github()
    elif "exit" in command.lower():
        print("Exiting program.")
        speak("Goodbye... Have a great day!")
    else:
        print("Command not recognized.")

greet()
while True:
    command = listen()
    if "exit" in command.lower():
        execute_command(command)
        break
    else:
        execute_command(command)