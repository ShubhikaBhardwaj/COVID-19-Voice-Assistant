import pyttsx3
import speech_recognition as sr


class VoiceAssistant:
    """ It is responsible for Voice Recognition and 'Text to Speech' conversion"""
    def __init__(self):
        # Initialise the python text to speech engine
        self.engine = pyttsx3.init()

        # Initialising ANSI Escape color codes
        self.BLUE = "\033[0;34m"
        self.RESET = "\033[0m"

    def speak(self, text):
        """Converts text to speak using the Python Speech Engine
        : param text: The sentence that has to be spoken by the Voice Assistant"""
        self.engine.say(text)
        print(f"\n{self.BLUE}COVID-19 Voice Assistant says: {text}{self.RESET}")
        self.engine.runAndWait()

    def get_audio(self):  # Listen
        """Listens to the user audio and,
         Converts speech to text """

        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            audio = recognizer.listen(source)
            said = ""

            try:
                # Google to recognize the speech input
                said = recognizer.recognize_google(audio)
            except Exception as e:
                self.speak("I didn't understand what you said. Please try once again!")
                print("Unable to understand what you just said.\nException:", str(e))
        return said.lower()
