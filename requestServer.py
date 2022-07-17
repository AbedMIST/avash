# source bin/activate
import urllib.request
import time
import speak
# import hear
import neckRotake
import threading
import alexa

voice = speak.Voice()
rotator = neckRotake.motor()
al = alexa.Alexa()
# ear = hear.Ear()
angle = 10
mn = 10

# def hear_thread(num):
#    ear.Hear()

#    print("thread started")

# t1 = threading.Thread(target=hear_thread, args=(10,))
# t1.start()

while True:
    angle, mn = rotator.rotate(angle, mn)
    print(angle, mn)

    f = urllib.request.urlopen('http://192.168.43.49:5050/moodFlg')

    x = f.read()
    x = x.decode('UTF-8')

    if x == "False":
        f = urllib.request.urlopen('http://192.168.43.49:5050/notiFlg')

        x = f.read()
        x = x.decode('UTF-8')

        if x == "False":
            time.sleep(3)
            continue
        else:
            f = urllib.request.urlopen('http://192.168.43.49:5050/notification')

            x = f.read()
            x = x.decode('UTF-8')
            print(x)
            voice.speak(x)
        print("server requested2")

        time.sleep(3)

    else:
        f = urllib.request.urlopen('http://192.168.43.49:5050/mood')

        x = f.read()
        x = x.decode('UTF-8')
        if x == "Happy":
            txt = "Avash ,  you are looking " + x + "Happiness is a now thing ,so Always try to be like this.I can play a song to give you more pleasure.Feel the song"
        elif x == "Neutral":
            txt = " Avash, you are now looking " + x + "You can go outside. Just a few minutes of fresh air can give you a fresh perspective"
        elif x == "Sad":
            txt = "Avash ,you are looking " + x + "No matter how bad things may seem, think positively. one of the quickest way to make yourself back up is to do something kind for someone else."
        elif x == "Surprise":
            txt = "Avash ,you are looking " + x + "you need not to be worry , be calm down. you should be ready for any kind of situation."

        print(txt)
        voice.speak(txt)

    # f = urllib.request.urlopen('http://192.168.43.49:5050/command')
    # x = f.read()
    # x = x.decode('UTF-8')
    # print (x)
    # voice.speak(x)
    # al.run_twin(command)

    print("server requested1")











