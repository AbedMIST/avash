class Voice:
    def __init__(self):
        print("voice object initialized")
    def moduledata(self):# this function contains information about this module
        print("Voice module info ***************")
        print("     Instruction ( get the instruction given by the user)")
        print("     Reminder ( will give the reminder)")
        print("     Text (convert voice to text)")
        print("end of info *****************")


import speech_recognition as sr
import pyaudio

r = sr.Recognizer()
while True:
    with sr.Microphone() as source:
        print("Speak Anything :")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print("You said : {}".format(text))
        except:
            print("Sorry could not recognize what you said")

