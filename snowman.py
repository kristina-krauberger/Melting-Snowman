from game_logic import play_game


def user_input():
    return input("Guess a letter: ").strip().lower()


def main():
    play_game(user_input)    #Hier wir die Funktion user_input() übergeben nicht das Ergebnis


if __name__ == "__main__":
    main()