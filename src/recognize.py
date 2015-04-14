import speech_recognition as sr
def callback(recognizer, audio):                          # this is called from the background thread
    print("trying to recognize")
    try:
        print(recognizer.recognize(audio))  # received audio data, now need to recognize it
    except LookupError:
        pass
r = sr.Recognizer()
r.listen_in_background(sr.Microphone(), callback)

import time
while True: time.sleep(0.1)
