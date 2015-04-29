import speech_recognition as sr
import re
from config import COMMANDS
import speech


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
                    if COMMANDS[key][1]:
                        speech.play_text(COMMANDS[key][0](args[0]))
                    else:
                        COMMANDS[key][0](args[0])
                else:
                    if COMMANDS[key][1]:
                        speech.play_text(COMMANDS[key][0]())
                    else:
                        COMMANDS[key][0]()
    except LookupError as e:
        speech.play_text("Could not recognize, please try again.")
        print('error', e)
        pass
r = sr.Recognizer()
r.listen_in_background(sr.Microphone(), callback)

import time
while True: time.sleep(0.1)
