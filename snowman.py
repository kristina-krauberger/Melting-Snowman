from game_logic import play_game


def get_input():
    while True:
        user_input = input("Guess a letter: ").strip().lower()

        if not user_input.isalpha() or len(user_input) != 1:
            print("Invalid input – please type **one single letter** (a-z).")
        else:
            return user_input


def main():
    play_game(get_input)    #Hier wir die Funktion get_input() übergeben nicht das Ergebnis


if __name__ == "__main__":
    main()