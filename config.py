from modules.weather.weather import get_weather
from modules.todo.todo import add_todo, list_todos
from modules.music.gs import play_song

COMMANDS = {
    "weather": get_weather,
    "what.* list": list_todos,
    "a\w (.*) to my list": add_todo,
    "play (.*)": play_song
}
