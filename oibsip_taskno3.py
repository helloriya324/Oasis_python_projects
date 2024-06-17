import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize speech recognition and text-to-speech engines
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    """Converts text to speech using pyttsx3."""
    engine.say(text)
    engine.runAndWait()

def get_audio():
    """Listens for user input using speech recognition."""
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        print("You said: " + text)
        return text.lower()  # Convert to lowercase for easier comparison
    except sr.UnknownValueError:
        print("Sorry, could not understand audio")
        return None
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return None

def process_command(text):
    """Processes user commands and performs actions."""
    if text in ("hello", "hi"):
        speak("Hello! How can I assist you today?")
    elif text == "time":
        speak(datetime.datetime.now().strftime('%I:%M %p'))  # Format time for better readability (e.g., 2:37 PM)
    elif text == "date":
        speak(datetime.date.today().strftime('%B %d, %Y'))  # Format date (e.g., June 16, 2024)
    elif "search for" in text:
        search_term = text.split("search for ")[-1]
        speak(f"Searching the web for {search_term}...")
        webbrowser.open(f"https://www.google.com/search?q={search_term}")
    else:
        speak("Sorry, I can't perform that action yet. But I'm always learning!")

# Main loop to continuously listen for commands
print("Starting Voice Assistant...")
while True:
    text = get_audio()
    if text:
        process_command(text)
        