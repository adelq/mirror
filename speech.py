from gtts import gTTS
import uuid
import subprocess

def save_text(text):
    tts = gTTS(text=text, lang='en')
    filename = "/tmp/{}.mp3".format(uuid.uuid4())
    tts.save(filename)
    return filename

def play_text(text):
    filename = save_text(text)
    subprocess.call(['cvlc', '--play-and-exit', '--rate', '1.1', filename])
