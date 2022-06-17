#pip install pydub
#apt-get install ffmpeg

from os import path
from pydub import AudioSegment

# files                                                                         
src = "twin.mp3"
dst = "twin.wav"

# convert wav to mp3                                                            
sound = AudioSegment.from_mp3(src)
sound.export(dst, format="wav")