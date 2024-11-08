from random import choice, randint
from hangman_game_module import hangman_game
import hangman_game_module
import importlib
from weather_api import return_weather_info

in_game = False

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()
    global in_game

    if in_game:
        if user_input == 'stop':
            in_game = False
            importlib.reload(hangman_game_module)
            return 'Thanks for game!'
        result = hangman_game(user_input)
        if result[:4] == 'stop':
            result = result[5:]
            importlib.reload(hangman_game_module)
            in_game = False
            return (f'{result}\n    '
                    f'Thanks for game!')
        return (f'{result}\n\n'
                f'Try to guess:')
    else:
        if 'hangman' in lowered or 'hm' in lowered:
            in_game = True
            return (f'Okayy, lets play:\n\n'
                    f'try to guess: ')
        elif 'hello' in lowered:
            return 'Hello there!'
        elif 'how are you' in lowered:
            return 'Good, thanks!'
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
