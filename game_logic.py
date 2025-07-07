import random
from ascii_art import STAGES
#from snowman import user_input WARUM FALSCH?

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    """Displays the snowman stage for the number of mistakes."""
    # Display the snowman stage for the current number of mistakes.
    print(STAGES[mistakes])
    # Build a display version of the secret word.
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word: ", display_word)
    print("\n")


def play_game(get_input):
    """
    Main game loop for Snowman Meltdown.
    The player tries to guess the secret word one letter at a time.
    - After 3 wrong guesses, the player loses.
    - If the full word is guessed, the player wins.
    """
    secret_word = get_random_word()
    print("\n\033[94m=== Welcome to SNOWMAN MELTDOWN! ===\033[0m\n")

    guessed_letters = []
    mistakes = 0
    has_won = False
    display_game_state(mistakes, secret_word, guessed_letters)

    while mistakes < 3 and not has_won:
        guess = get_input()

        # Checks duplicates and appends guessed letter.
        if guess in guessed_letters:
            print("\033[91mYou already guessed that letter\033[0m")

        else:
            guessed_letters.append(guess)

        # Checks the number of mistakes.
        if guess not in secret_word:
            mistakes += 1

        display_game_state(mistakes, secret_word, guessed_letters)
        print("You guessed:", guess)

        # Checks if the word was guessed correctly.
        has_won = True
        for letter in secret_word:
            if letter not in guessed_letters:
                has_won = False
                break

    # Ends Game
    if has_won:
        print(f"\033[92m***** YOU WIN! The word was {secret_word} *****\033[0m")
        print("\033[92m***** You have saved the snowman! *****\033[0m")
    else:
        print(f"\033[91m***** GAME OVER! The word was: {secret_word} *****\033[0m")
        print("\033[91m***** You have melted the snowman! *****\033[0m")



