from random import choice, randint
from weather_api import return_weather_info


def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if 'hello' in lowered:
        return 'Hello there!'
    elif 'bye' in lowered:
        return 'See you!'
    elif 'roll dice' in lowered:
        return f'You rolled: {randint(1, 6)}'
    elif 'temp' in lowered:
        lowered.split()
        weather_info = return_weather_info(lowered[lowered.index('temp') + 1])
        return weather_info
    else:
        pass