from modules.weather.weather import get_weather
from modules.todo.todo import add_todo, list_todos
from modules.music.gs import play_song

# Tuple is function name, and boolean whether it should be spoken as text
COMMANDS = {
    "weather": (get_weather, True),
    "what.* list": (list_todos, True),
    "a\w+ (.*) to my list": (add_todo, True),
    "play (.*)": (play_song, False)
}
