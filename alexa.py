import sys

import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import keyboard  # using module keyboard
from pynput.keyboard import Listener
import pyautogui

# pip install pyttsx3
# pip install pyjokes
# apt install libespeak-dev

flag = 1
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    print(text)
    engine.runAndWait()


def take_command():
    try:
        command = "-1"
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'twin' in command:
                command = command.replace('twin', '')
                print(command)

        return command
    except:
        pass


# twin

def run_twin():
    try:
        command = take_command()
        if command != "-1":
            print(command)
            if 'play' in command:
                song = command.replace('play', '')
                talk('playing ' + song)
                pywhatkit.playonyt(song)  # Playing song from youtube
            elif 'time' in command:
                time = datetime.datetime.now().strftime('%I:%M %p')
                talk('Current time is ' + time)
            elif 'who the heck is' in command:
                person = command.replace('who the heck is', '')
                info = wikipedia.summary(person, 1)
                print(info)
                talk(info)
            elif 'date' in command:
                talk('sorry, I have a headache')
            elif 'are you single' in command:
                talk('I am in a relationship with wifi')
            elif 'joke' in command:
                talk(pyjokes.get_joke())
            else:
                talk('Please say the command again.')
    except:
        pass


cnt = 0
while flag == 1:

    # flag = input("to break loop enter '0': ")
    print("Looping " , flag)
    if keyboard.is_pressed("q"):  # if key 's' is pressed
        flag = 0
        exit()
        sys.exit()
    try:
        print("In tryyy")
        run_twin()
    except:
        pass
