import speech_recognition as sr
import re
from modules.weather import weather


def callback(recognizer, audio):                          # this is called from the background thread
    print("trying to recognize")
    try:
        text = recognizer.recognize(audio)  # received audio data, now need to recognize it
        print(text)
        if re.search("weather", text):
            print(weather.get_weather())
    except LookupError:
        print('error')
        pass
r = sr.Recognizer()
r.listen_in_background(sr.Microphone(), callback)

import time
while True: time.sleep(0.1)
