from game_logic import play_game

RED = "\033[91m"
BLUE = "\033[94m"
RESET = "\033[0m"


def get_input():
    """
    Prompts the user to input a single alphabetical letter.
    Validates that the input is exactly one character (a-z).
    :return: str: A valid single lowercase letter.
    """
    while True:
        try:
            user_input = input("Guess a letter: ").strip().lower()

            if not user_input.isalpha() or len(user_input) != 1:
                raise ValueError("Please type **one single letter** (a-z).")

            return user_input

        except ValueError as e:
            print(f"{RED}Invalid input – {e}{RESET}")


def main():
   while True:
        play_game(get_input)
        again = input(f"\n{BLUE}Do you want to play again? (y/n): {RESET}").strip().lower()
        if again != "y":
            print(f"{BLUE}Thanks for playing! Goodbye!️{RESET}")
            break


if __name__ == "__main__":
    main()