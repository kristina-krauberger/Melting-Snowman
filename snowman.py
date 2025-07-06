import random

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def play_game():
    """
    Main game loop for Snowman Meltdown.
    The player tries to guess the secret word one letter at a time.
    - After 3 wrong guesses, the player loses.
    - If the full word is guessed, the player wins.
    """
    secret_word = get_random_word()
    print("Welcome to Snowman Meltdown!")
    print("Secret word selected: " + secret_word)  # for testing, later remove this line

    # TODO: Build your game loop here.
    # For now, simply prompt the user once:
    guessed_letters = []
    for i in range(len(secret_word)):
        guess = input("Guess a letter: ").strip().lower()
        guessed_letters.append(guess)
        print("You guessed:", guess)
        print(guessed_letters)
    if set(guessed_letters) == set(secret_word):
        print(f"You Win! The word was {secret_word}")
    else:
        print(f"Game Over! The word was: {secret_word}")


if __name__ == "__main__":
    play_game()