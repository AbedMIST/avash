import speech_recognition as sr # pip3 install SpeechRecognition pydub


filename = "twin.wav"
# initialize the recognizer
r = sr.Recognizer()
with sr.AudioFile(filename) as source:
    # listen for the data (load audio to memory)
    audio_data = r.record(source)
    # recognize (convert from speech to text)
    text = r.recognize_google(audio_data)
    print(text)