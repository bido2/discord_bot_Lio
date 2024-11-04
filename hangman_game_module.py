from random import random


draw_list = [
    f'/',
    f'/|',
    f'/|\\',
    f' | \n/|\\ \n',
    f' | \n | \n/|\\ \n',
    f' | \n | \n | \n/|\\ \n',
    f' | \n | \n | \n | \n/|\\ \n',
    f' | \n | \n | \n | \n | \n/|\\ \n',
    f' ________ \n | \n | \n | \n | \n | \n/|\\ \n',
    f' ________ \n |      |\n | \n | \n | \n | \n/|\\ \n',
    f' ________ \n |      |\n |      o\n | \n | \n | \n/|\\ \n',
    f' ________ \n |      |\n |      o\n |     /|\\ \n | \n | \n/|\\ \n',
    f' ________ \n |      |\n |      o\n |     /|\\ \n |     / \\ \n | \n/|\\ \n',
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

password = 'kot'

user_guesses = []

def hangman_game(guess: str):
    guess.lower()
    global lives_lost
    global draw_list
    global password
    global user_guesses

    if guess in password:
        user_guesses += guess
        return f'brawo, {guess} jest w haśle'
    else:
        lives_lost+=1
        user_guesses += guess
        print(draw_list[lives_lost-1])
        return f'{guess} nie ma w haśle \n{draw_list[lives_lost-1]}'

