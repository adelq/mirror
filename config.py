from modules.weather.weather import get_weather
from modules.todo.todo import add_todo, list_todos
from modules.music.gs import play_song

COMMANDS = {
    "weather": get_weather,
    "list to do": list_todos
}
