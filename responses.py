from random import choice, randint
from hangman_game_module import hangman_game

in_game = False

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()
    global in_game
    if in_game:
        result = hangman_game(user_input)
        return f'{result}\n\nZgaduj:'
    else:
        if lowered == '':
            return None
        elif 'hangamn' in lowered:
            in_game = True
            return 'Okay, lets play:)\n\nZgaduj:'
        elif 'hello' in lowered:
            return 'Hello there!'
        elif 'how are you' in lowered:
            return 'Good, thanks!'
        elif 'bye' in lowered:
            return 'See you!'
        elif 'roll dice' in lowered:
            return f'You rolled: {randint(1, 6)}'
        else:
            return choice(['I do not understand...',
                           'What are you talking about?',
                           'Do you mind rephrasing that?'])