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
        speak("Good morning Sir! Allow me to introduce myself. I am Jarvis, your AI assistant.")
    elif 12 <= hour < 18:
        speak("Good afternoon Sir! Allow me to introduce myself. I am Jarvis, your AI assistant.")
    else:
        speak("Good evening Sir! Allow me to introduce myself. I am Jarvis, your AI assistant.")

# Open Applications - Dictionary-based approach
APPLICATIONS = {
    "google": {
        "command": "start chrome",
        "speech": "Opening Google"
    },
    "edge": {
        "command": "start msedge",
        "speech": "Opening Edge"
    },
    "youtube": {
        "command": "start chrome https://www.youtube.com/",
        "speech": "Opening Youtube"
    },
    "spotify": {
        "command": "start spotify",
        "speech": "Opening Spotify"
    },
    "word": {
        "command": "start winword",
        "speech": "Opening Word"
    },
    "powerpoint": {
        "command": "start powerpnt",
        "speech": "Opening PowerPoint"
    },
    "excel": {
        "command": "start excel",
        "speech": "Opening Excel"
    },
    "calculator": {
        "command": "start calc",
        "speech": "Opening Calculator"
    },
    "notepad": {
        "command": "start notepad",
        "speech": "Opening Notepad"
    },
    "github": {
        "command": "start chrome https://github.com/",
        "speech": "Opening Github"
    },
    "discord": {
        "command": "start chrome https://discord.com/",
        "speech": "Opening Discord"
    },
    "command prompt": {
        "command": "start cmd",
        "speech": "Opening Command Prompt"
    },
    "file explorer": {
        "command": "start explorer",
        "speech": "Opening File Explorer"
    },
    "vs code": {
        "command": "start code",
        "speech": "Opening Visual Studio Code"
    },
    "visual studio code": {
        "command": "start code",
        "speech": "Opening Visual Studio Code"
    },
    "paint": {
        "command": "start mspaint",
        "speech": "Opening Paint"
    },
    "settings": {
        "command": "start ms-settings:",
        "speech": "Opening Settings"
    },
    "task manager": {
        "command": "start taskmgr",
        "speech": "Opening Task Manager"
    }
}

def open_application(app_name):
    """Open an application based on its name."""
    if app_name in APPLICATIONS:
        app_info = APPLICATIONS[app_name]
        speak(app_info["speech"])
        os.system(app_info["command"])
        return True
    return False

# Utility Functions
def get_time():
    """Get current time."""
    now = datetime.datetime.now()
    time_str = now.strftime("%I:%M %p")
    speak(f"The time is {time_str}")
    print(f"Time: {time_str}")

def get_date():
    """Get current date."""
    now = datetime.datetime.now()
    date_str = now.strftime("%B %d, %Y")
    day = now.strftime("%A")
    speak(f"Today is {day}, {date_str}")
    print(f"Date: {day}, {date_str}")

def search_web(query):
    """Search the web for a query."""
    speak(f"Searching for {query}")
    search_url = f"start chrome https://www.google.com/search?q={query.replace(' ', '+')}"
    os.system(search_url)

def get_system_info():
    """Get basic system information."""
    import platform
    system = platform.system()
    release = platform.release()
    machine = platform.machine()
    speak(f"You are running {system} {release} on {machine} architecture")
    print(f"System: {system} {release}")
    print(f"Architecture: {machine}")

def shutdown_system():
    """Shutdown the system."""
    speak("Shutting down the system in 30 seconds. Say cancel to abort.")
    os.system("shutdown /s /t 30")

def restart_system():
    """Restart the system."""
    speak("Restarting the system in 30 seconds. Say cancel to abort.")
    os.system("shutdown /r /t 30")

def cancel_shutdown():
    """Cancel scheduled shutdown or restart."""
    speak("Shutdown cancelled")
    os.system("shutdown /a")

# Execute Commands
def execute_command(command):
    # Check for exit command
    if "exit" in command or "quit" in command or "bye" in command:
        speak("Goodbye! Have a great day!")
        exit()
    
    # Time and Date queries
    if "time" in command:
        get_time()
        return
    
    if "date" in command or "today" in command:
        get_date()
        return
    
    # System commands
    if "system info" in command or "system information" in command:
        get_system_info()
        return
    
    if "shutdown" in command:
        shutdown_system()
        return
    
    if "restart" in command or "reboot" in command:
        restart_system()
        return
    
    if "cancel" in command:
        cancel_shutdown()
        return
    
    # Web search
    if "search for" in command or "search" in command:
        # Extract search query
        if "search for" in command:
            query = command.split("search for", 1)[1].strip()
        else:
            query = command.split("search", 1)[1].strip()
        if query:
            search_web(query)
            return
    
    # Check for "open" commands
    if "open" in command:
        # Extract the app name after "open"
        words = command.split()
        if "open" in words:
            open_index = words.index("open")
            # Get everything after "open" as the app name
            app_name = " ".join(words[open_index + 1:])
            
            # Try to open the application
            if open_application(app_name):
                return  # Successfully opened
    
    # If command not recognized, ask Gemini
    print("Command not recognized. Asking Google Gemini...")
    speak("I am not sure, let me check.")
    response = get_gemini_response(command)
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

