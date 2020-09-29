from gtts import gTTS
import os

file = open("sample.txt")
f = file.read()

language = 'en'

audio = gTTS(text=f, lang=language, slow="false")

audio.save("aud.wav")
os.system("aud.wav")
