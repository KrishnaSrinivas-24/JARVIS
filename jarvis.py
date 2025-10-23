import google.generativeai as genai
import speech_recognition as sr
import pyttsx3
import datetime
import os

# Set up Gemini API Key (Replace with your actual API key)
genai.configure(api_key="Paste your API Here")

# Text-to-Speech
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Speech Recognition
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Could not understand audio")
            speak("Sorry, I didn't catch that.")
            return None
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            speak("I'm having trouble with the speech service.")
            return None
        except sr.WaitTimeoutError:
            print("Listening timed out")
            return None

# Wake Word Detection
def listen_for_wake_word():
    """Listen for the wake word 'Hey Jarvis' or 'Jarvis' to activate the assistant."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Waiting for wake word... (Say 'Hey Jarvis' or 'Jarvis')")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        try:
            audio = recognizer.listen(source, timeout=10, phrase_time_limit=5)
            text = recognizer.recognize_google(audio).lower()
            print(f"Heard: {text}")
            
            # Check for wake words
            if "hey jarvis" in text or "jarvis" in text or "hey" in text:
                print("Wake word detected!")
                speak("Yes? How can I help you?")
                return True
            return False
        except sr.UnknownValueError:
            return False
        except sr.RequestError:
            return False
        except sr.WaitTimeoutError:
            return False
        except Exception:
            return False

# Google Gemini AI Response
def get_gemini_response(prompt):
    try:
        model = genai.GenerativeModel("gemini-pro")  # Using "gemini-pro" for text generation
        response = model.generate_content(prompt)
        return response.text  # Extract the response text
    except Exception as e:
        print(f"Error getting Gemini response: {e}")
        return "I'm having trouble connecting to my knowledge base right now."

# Greet User
def greet():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good morning! Allow me to introduce myself. I am Jarvis, your AI assistant.")
    elif 12 <= hour < 18:
        speak("Good afternoon! Allow me to introduce myself. I am Jarvis, your AI assistant.")
    else:
        speak("Good evening! Allow me to introduce myself. I am Jarvis, your AI assistant.")

# Open Applications
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
    os.system("start winword")

def open_powerpoint():
    speak("Opening PowerPoint")
    os.system("start powerpnt")

def open_excel():
    speak("Opening Excel")
    os.system("start excel")

def open_calculator():
    speak("Opening Calculator")
    os.system("start calc")

def open_notepad():
    speak("Opening Notepad")
    os.system("start notepad")

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

# Execute Commands
def execute_command(command):
    if "open google" in command:
        open_google()
    elif "open edge" in command:
        open_edge()
    elif "open spotify" in command:
        open_spotify()
    elif "open youtube" in command:
        open_youtube()
    elif "open word" in command:
        open_word()
    elif "open discord" in command:
        open_discord()
    elif "open notepad" in command:
        open_notepad()
    elif "open powerpoint" in command:
        open_powerpoint()
    elif "open excel" in command:
        open_excel()
    elif "open calculator" in command:
        open_calculator()
    elif "open command prompt" in command:
        open_command_prompt()
    elif "open file explorer" in command:
        open_file_explorer()
    elif "open github" in command:
        open_github()
    elif "exit" in command:
        speak("Goodbye! Have a great day!")
        exit()
    else:
        print("Command not recognized. Asking Google Gemini...")
        speak("I am not sure, let me check.")
        response = get_gemini_response(command)  # Ask Gemini for an answer
        print(f"Gemini: {response}")
        speak(response)

# Start JARVIS
greet()

# Ask user for preferred mode
print("\nSelect listening mode:")
print("1. Wake Word Mode (Say 'Hey Jarvis' to activate)")
print("2. Always Listening Mode (No wake word required)")
mode_choice = input("Enter your choice (1 or 2, default is 2): ").strip()

use_wake_word = (mode_choice == "1")

if use_wake_word:
    print("\n🎤 Wake Word Mode Enabled")
    print("Say 'Hey Jarvis' or 'Jarvis' to activate the assistant.")
    print("Say 'exit' to quit.\n")
else:
    print("\n🎤 Always Listening Mode Enabled")
    print("JARVIS is ready. Say 'exit' to quit.\n")

while True:
    if use_wake_word:
        # Wait for wake word
        if listen_for_wake_word():
            # Wake word detected, listen for command
            command = listen()
            if command:
                execute_command(command)
    else:
        # Always listening mode (original behavior)
        command = listen()
        if command:
            execute_command(command)

