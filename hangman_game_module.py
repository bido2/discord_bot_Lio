import random

def findIndexOf(list, x):
    result = []
    for index in range(len(list)):
        if list[index] == x:
            result.append(index)
    return result

def password_dispaly(password):
    dispaly = ''
    for i in password:
        dispaly+= i + ' '
    return dispaly




draw_list = [
    f'/',
    f'/|',
    f'/|\\',
    f' | \n/|\\ \n',
    f' | \n | \n/|\\ \n',
    f' | \n | \n | \n/|\\ \n',
    f' | \n | \n | \n | \n/|\\ \n',
    f' | \n | \n | \n | \n | \n/|\\ \n',
    f'    ________ \n  | \n | \n | \n | \n | \n/|\\ \n',
    f'    ________ \n  |      |\n | \n | \n | \n | \n/|\\ \n',
    f'    ________ \n  |      |\n |      o\n | \n | \n | \n/|\\ \n',
    f'    ________ \n  |      |\n |      o\n |     /|\\ \n | \n | \n/|\\ \n',
    f'    ________ \n  |      |\n |      o\n |     /|\\ \n |     / \\ \n | \n/|\\ \n',
]
lives_lost = 0

words_list = ["kot", "pies", "drzewo", "komputer", "klawiatura", "telefon", "okno", "słońce", "książka", "szkoła",
              "dom", "biurko", "chmura", "jabłko", "telefon", "sztuka", "noc", "dzień", "morze", "ogródek",
              "woda", "miasto", "muzyka", "obraz", "ogród", "kwiat", "samochód", "ulica", "słowo", "język",
              "obiad", "kolacja", "rower", "deszcz", "śnieg", "sklep", "praca", "nauka", "uczeń", "nauczyciel",
              "język", "twarz", "kawa", "herbata", "kanapka", "zima", "wiosna", "lato", "jesień", "papier",
              "zeszyt", "stół", "okulary", "nóż", "widelec", "łyżka", "czapka", "szalik", "buty", "słuchawki",
              "telewizja", "radio", "internet", "kabel", "myszka", "projekt", "piłka", "ręka", "nogi", "głowa",
              "zegar", "pociąg", "samolot", "plaża", "jezioro", "człowiek", "dziecko", "wiatrak", "klimat",
              "mikrofon", "głośnik", "księżyc", "zabawa", "miłość", "sztuka", "teatr", "film", "opowiadanie",
              "powieść", "obraz", "zdjęcie", "matematyka", "fizyka", "chemia", "biologia", "geografia", "historia"]

password = [char for char in words_list[random.randint(0,99)]]
copy_password = list(password)
for index in range(len(copy_password)):
    copy_password[index] = '#'

user_guesses = []

def hangman_game(guess: str):
    guess.lower()
    global lives_lost
    global draw_list
    global password
    global user_guesses
    global copy_password

    print(copy_password)

    if not guess.isalpha() or len(guess) != 1:
        return 'It\'s not a letter :<, Try again'
    elif guess in user_guesses:
        return 'You already tried that letter, Try again'
    elif guess in password:
        user_guesses += guess
        index_of_guess_list = findIndexOf(password, guess)
        for index in index_of_guess_list:
            copy_password[index] = guess
        if copy_password == list(password):
            return f'stop Confratulatios! you won, password was: {password}'
        if lives_lost >0:
            draw = draw_list[lives_lost-1]
        else:
            draw = ''
        return (f'Nice! {guess} is in the password\n'
                f'{password_dispaly(copy_password)}\n'
                f'Your guesses: {user_guesses}\n'
                f'{draw}')
    else:
        lives_lost+=1
        if lives_lost == 13:
            return (f'stop {draw_list[lives_lost-1]}\n'
                    f'You lost:(')
        user_guesses += guess
        draw = (draw_list[lives_lost-1])
        return (f'Oops, {guess} isn\'t in the password\n'
                f'{password_dispaly(copy_password)}\n'
                f'Your guesses: {user_guesses}\n'
                f'{draw}')

