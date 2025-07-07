import random

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

# Snowman ASCII Art stages
STAGES = [
     # Stage 0: Full snowman
     """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
     ( : ) 
     """,
     # Stage 1: Bottom part starts melting
     """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
     """,
     # Stage 2: Only the head remains
     """
      ___  
     /___\\ 
     (o o) 
     """,
     # Stage 3: Snowman completely melted
     """
      ___  
     /___\\ 
     """
 ]

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


    guessed_letters = []
    mistakes = 0
    display_game_state(mistakes, secret_word, guessed_letters)

    while mistakes < 3:
         guess = input("Guess a letter: ").strip().lower()

         #checks and appends guessed letter
         if guess in guessed_letters:
             print("You already guessed that letter")
         else:
            guessed_letters.append(guess)

        #checks the number of mistakes
         if guess not in secret_word:
             mistakes += 1

         display_game_state(mistakes, secret_word, guessed_letters)
         print("You guessed:", guess)

    if set(guessed_letters) == set(secret_word):
        print(f"You Win! The word was {secret_word}")
    else:
        print(f"Game Over! The word was: {secret_word}")


if __name__ == "__main__":
    play_game()