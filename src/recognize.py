import speech_recognition as sr
import re
from subprocess import call
from config import COMMANDS


def callback(recognizer, audio):
    print("trying to recognize")
    try:
        text = recognizer.recognize(audio)
        print(text)
        for key in COMMANDS:
            if re.search(COMMANDS[key], text):
                COMMANDS[key]()
    except LookupError:
        print('error')
        pass
r = sr.Recognizer()
r.listen_in_background(sr.Microphone(), callback)

import time
while True: time.sleep(0.1)
