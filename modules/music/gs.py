import subprocess
from grooveshark import Client

client = Client()
client.init()

def get_song_url(song_name):
    song = client.search(song_name).next()
    return song.stream.url

def play_song_url(song_url):
    subprocess.call(['cvlc', song_url])

def play_song(song_name):
    play_song_url(get_song_url(song_name))
