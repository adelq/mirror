import os
import pyowm

owm = pyowm.OWM(os.getenv('OWM_KEY'))

def get_weather(loc="Philadelphia,PA"):
    obs = owm.weather_at_place(loc)
    w = obs.get_weather()
    temp = int(round(w.get_temperature("fahrenheit")["temp"]))
    cond = w.get_status()
    print("The temperature is {} degrees and {}".format(temp, cond))
