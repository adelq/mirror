import speech_recognition as sr
import re
from subprocess import call
from config import COMMANDS


def callback(recognizer, audio):
    print("trying to recognize")
    try:
        text = recognizer.recognize(audio)
        print text
        for key in COMMANDS:
            match = re.search(key, text)
            if match:
                args = match.groups()
                print 'args', args
                print 'found', key
                if (len(args) > 0):
                    COMMANDS[key](args[0])
                else:
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
