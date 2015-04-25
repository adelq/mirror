import speech_recognition as sr
import re
from subprocess import call
import pdb; pdb.set_trace()
# from config import COMMANDS


def callback(recognizer, audio):
    print("trying to recognize")
    try:
        text = recognizer.recognize(audio)
        for key in COMMANDS:
            if re.search(key, text):
                print 'found', key
                COMMANDS[key]()
    except LookupError:
        print('error')
        pass
r = sr.Recognizer()
r.listen_in_background(sr.Microphone(), callback)

from modules.todo.todo import add_todo, list_todos
add_todo('work')
add_todo('eat')

import time
while True: time.sleep(0.1)
