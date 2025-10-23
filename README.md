# JARVIS - Just A Rather Very Intelligent System

A Python-based voice assistant that can execute commands, open applications, and answer questions using Google's Gemini AI.

## Features

✨ **Voice Commands** - Control your computer with natural speech
🎤 **Continuous Listening** - Always ready without restart delays
🤖 **AI-Powered** - Uses Google Gemini for intelligent responses
🚀 **Quick Actions** - Open apps, browsers, and system tools instantly

## Installation

1. Clone the repository:
```bash
git clone https://github.com/KrishnaSrinivas-24/JARVIS.git
cd JARVIS
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your Google Gemini API key:
   - Get your API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Replace `"Paste your API Here"` in `jarvis.py` with your actual API key

## Usage

Run JARVIS:
```bash
python jarvis.py
```

You'll be prompted to choose a listening mode:
- **Option 1: Wake Word Mode** - Say "Hey Jarvis" or "Jarvis" to activate
- **Option 2: Always Listening Mode** - No wake word needed (default)

### Wake Word Mode

When using wake word mode:
1. Wait for the prompt: `Waiting for wake word...`
2. Say **"Hey Jarvis"** or **"Jarvis"**
3. JARVIS will respond: "Yes? How can I help you?"
4. Give your command
5. Repeat for each command

**Benefits:**
- Privacy-friendly - only listens when activated
- Saves battery on laptops
- Reduces false positives in noisy environments

### Available Commands

**Open Applications:**
- "Open Google" / "Open Edge" - Launch browsers
- "Open YouTube" / "Open Spotify" - Media platforms
- "Open Word" / "Open Excel" / "Open PowerPoint" - Office apps
- "Open Notepad" / "Open Calculator" - System utilities
- "Open GitHub" / "Open Discord" - Dev tools
- "Open Command Prompt" / "Open File Explorer" - System access

**Exit:**
- "Exit" - Close JARVIS

**General Questions:**
- Ask anything! If JARVIS doesn't recognize a command, it will use Gemini AI to answer your question.

## Recent Improvements

### Wake Word Detection (Issue #2)
- ✅ Added optional wake word mode with "Hey Jarvis" or "Jarvis" activation
- ✅ User can choose between wake word mode and always-on mode at startup
- ✅ Improved privacy - only listens when wake word is detected
- ✅ Better battery efficiency for laptops
- ✅ Reduced false positives in noisy environments

### Continuous Listening Optimization (Issue #1)
- ✅ Removed recursive restart after unknown responses
- ✅ Added proper error handling for all speech recognition exceptions
- ✅ Implemented timeout and phrase limits to prevent hanging
- ✅ Added ambient noise adjustment for better recognition
- ✅ Continuous loop without restart delays

**Benefits:**
- No more infinite loops on recognition errors
- Faster response time between commands
- Better error recovery
- Smoother user experience
- Privacy-friendly wake word option

## Requirements

- Python 3.7+
- Microphone access
- Internet connection (for speech recognition and Gemini AI)
- Windows OS (for application shortcuts)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.
