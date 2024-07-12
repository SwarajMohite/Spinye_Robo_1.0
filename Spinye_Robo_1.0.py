# Spinye Robo 1.0 created by Swaraj Mohite

# Required packages: pyttsx3, pyjokes, google_trans_new, SpeechRecognition
# Install using:
# pip install pyttsx3 pyjokes google_trans_new SpeechRecognition

import pyttsx3  # Module to speak the text
import pyjokes  # To generate Random Jokes
from google_trans_new import google_translator # Module to Translate New.
from translate import Translator # To translate
import googletrans # Module to Translate
import speech_recognition as SR # Module for Speech functionality

def intro(user_name):
    """
    Introduction of Spinye to the user. About its usage.
    """
    intro_message = f'''
    Hello {user_name}! You can interact with me by typing commands or speaking to me.
    You can ask me to do various things like translate or tell jokes.
    You can find out what I can do at any time by typing 'help'.
    Let's get started!
    '''
    print(intro_message)
    SpeakIT.say(intro_message)
    SpeakIT.runAndWait()

def show_help():
    """
    Show the help message i.e listing available commands.
    """
    help_message = '''
    Available commands:
    1. Enter any text to hear it spoken by me
    2. Enter 'quit' to quit.
    3. Enter 'voice' to set voice.
    4. Enter 'rate' to change Speech Rate
    5. Enter 'volume' to set volume of Speech
    6. Enter 'joke' to hear a joke.
    7. Enter 'help' to see this help message.
    8. Enter 'clear' to clear previously entered commands
    9. Enter 'open' to see previously entered commands
    10. Enter 'trans' to translate text to another language
    11. Enter 'vtrans' to start voice translator to translate and speak text.
    '''
    print(help_message)
    SpeakIT.say(help_message)
    SpeakIT.runAndWait()

def set_voice(SpeakIT):
    """
    Set the voice of the speech engine. i.e Male or Female
    """
    voices = SpeakIT.getProperty('voices')
    print("Available voices: \n")
    SpeakIT.say("Available voices")
    SpeakIT.runAndWait()
    for index, voice in enumerate(voices):
        print(f"{index}: {voice.name}")
    choice = input("Enter the number of the voice you want: ")
    if choice.isdigit() and 0 <= int(choice) < len(voices):
        SpeakIT.setProperty('voice', voices[int(choice)].id)
        SpeakIT.say("Voice changed successfully!")
        SpeakIT.runAndWait()
    else:
        print("Invalid input. Please enter a valid number.")

def set_rate(SpeakIT):
    """
    Set the speech rate of the speech engine.
    """
    rate = input("Enter the speech rate (Default is 200): ")
    if rate.isdigit():
        SpeakIT.setProperty('rate', int(rate))
    else:
        print("Invalid input. Please enter a valid number.")

def set_volume(SpeakIT):
    """
    Set the volume of the speech engine.
    """
    volume = input("Enter the desired volume between 0.0 and 1.0: ")
    try:
        volume = float(volume)
        if 0.0 <= volume <= 1.0:
            SpeakIT.setProperty('volume', volume)
        else:
            print("Invalid input. Please enter a valid number between 0.0 and 1.0.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def tell_joke():
    """
    Tell a random joke using the pyjokes module.
    """
    joke = pyjokes.get_joke()
    print(joke)
    SpeakIT.say(joke)
    SpeakIT.runAndWait()

def my_commands(command):
    """
    Save the user's commands to a file my_commands.txt .
    """
    with open("my_commands.txt", "a") as file:
        file.write(command + "\n")

def clear_file():
    """
    Clear the saved commands from the file my_commands.txt .
    """
    with open("my_commands.txt", "w") as file:
        file.write("")
    print("Commands cleared from file.")
    SpeakIT.say("Commands cleared from file.")
    SpeakIT.runAndWait()

def list_commands():
    """
    Shows the list of previously entered commands from the file.
    """
    print("Previously entered commands: \n")
    SpeakIT.say("Previously entered commands")
    SpeakIT.runAndWait()
    with open("my_commands.txt") as file:
        commands = file.readlines()
        for command in commands:
            print(command.strip())
            SpeakIT.say(command.strip())
            SpeakIT.runAndWait()

def translate():
    """
    Translate text to another language using google_translator.
    """
    lang_choice = input("\nDo you want a list of language codes (y/n) to enter the language you are typing: ")
    if lang_choice.lower() == "y":
        languages = googletrans.LANGUAGES
        print("Available languages:\n")
        for code, language in languages.items():
            print(f"{language.title()}: {code}")

    lang_from = input("Enter the language code you are typing: (en for english) : ")
    text_to_translate = input("Enter the text to translate: ")

    lang_choice = input("\nDo you want a list of language codes (y/n) to enter the desired language: ")
    if lang_choice.lower() == "y":
        for code, language in googletrans.LANGUAGES.items():
            print(f"{language.title()}: {code}")

    lang_to = input("Enter the target language code: (mr for marathi, fr for french) : ")

    try:
        translator = Translator(from_lang=lang_from, to_lang=lang_to)
        translated = translator.translate(text_to_translate)
        print(f"Translated text: {translated}")
        SpeakIT.say(translated)
        SpeakIT.runAndWait()
    except Exception as e:
        error = "Sorry! I couldn't translate the text!"
        print(f"{error} Error: {e}")
        SpeakIT.say(error)
        SpeakIT.runAndWait()


def voice_translate():
    """
    Translate spoken language (english) to another language using google_translator and speech_recognition.
    """
    recognizer = SR.Recognizer()
    translator = google_translator()
    
    try:
        with SR.Microphone() as source:
            lang_choice = input("\nDo you want a list of language codes (y/n) to enter the language you are speaking: ")
            if lang_choice.lower() == "y":
                languages = googletrans.LANGUAGES
                print("Available languages:\n")
                for code, language in languages.items():
                    print(f"{language.title()}: {code}")

            lang_from = input("Enter the language code you are speaking: (en for English) : ")

            print("Clearing the background noise....")
            SpeakIT.say("Clearing the background noise....")
            SpeakIT.runAndWait()
            recognizer.adjust_for_ambient_noise(source, duration=1)

            print("Speak something...")
            SpeakIT.say("Speak something...")
            SpeakIT.runAndWait()
            audio = recognizer.listen(source, timeout=10)  # Increased timeout duration
            print("Done Recording...")
            SpeakIT.say("Done Recording...")
            SpeakIT.runAndWait()

        print("Recognizing speech...")
        SpeakIT.say("Recognizing speech...")
        SpeakIT.runAndWait()
        text = recognizer.recognize_google(audio, language=lang_from)
        print(f"You said: {text}")

        lang_choice = input("\nDo you want a list of language codes (y/n) to enter the desired language: ")

        if lang_choice.lower() == "y":
            for code, language in googletrans.LANGUAGES.items():
                print(f"{language.title()}: {code}")

        lang_to = input("Enter the target language code: (fr for french , mr for Marathi) : ")
        translator = Translator(from_lang=lang_from, to_lang=lang_to)
        translated = translator.translate(text)
        print(f"Translated text: {translated}")
        SpeakIT.say(translated)
        SpeakIT.runAndWait()
    
    except Exception as e:
        error = "Sorry! I couldn't translate the text!"
        print(f"{error} Error: {e}")
        SpeakIT.say(error)
        SpeakIT.runAndWait()


if __name__ == '__main__':
    """
    Main function. 
    """
    SpeakIT = pyttsx3.init()
    voices = SpeakIT.getProperty('voices')
    SpeakIT.setProperty('voice', voices[0].id)  # Set default voice at 0th position i.e. 1st element

    print("Welcome to Spinye 1.0 created by Swaraj!")
    SpeakIT.say("Welcome to Spinye 1.0 created by Swaraj!")
    SpeakIT.runAndWait()

    user_name = input("Please enter your name: ")
    SpeakIT.say(f"Hello, {user_name}!")
    SpeakIT.runAndWait()

    intro(user_name)

    while True:
        command = input("Enter the command or text which you want me to speak: ")
        my_commands(command)

        # calling different functions
        if command.lower() == "quit":
            SpeakIT.say(f"Goodbye, {user_name}!")
            SpeakIT.runAndWait()
            break
        elif command.lower() == "voice":
            set_voice(SpeakIT)
        elif command.lower() == "joke":
            tell_joke()
        elif command.lower() == "rate":
            set_rate(SpeakIT)
        elif command.lower() == "volume":
            set_volume(SpeakIT)
        elif command.lower() == "clear":
            clear_file()
        elif command.lower() == "open":
            list_commands()
        elif command.lower() == "help":
            show_help()
        elif command.lower() == "trans":
            translate()
        elif command.lower() == "vtrans":
            voice_translate()
        else:
            SpeakIT.say(command)
            SpeakIT.runAndWait()


# The Spinye Robo 1.0 AI program is a powerful tool designed to enhance communication, learning, and entertainment. Its diverse features make it suitable for a wide range of users, from those with speech impairments to language learners and professionals working in multilingual environments. By integrating text-to-speech, translation, and interactive capabilities, the program offers practical solutions to everyday challenges in communication and accessibility.c