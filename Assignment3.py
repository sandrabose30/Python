# Hangman Game

import time
def countdown():
    print("Countdown begins...")
    for i in range(3, 0, -1):
        print(i)
        time.sleep(1)
    print("Start!\n")

def hangman_game():
    print("-----------------------------------")
    print("        Hangman Game - Welcome     ")
    print("      Find Malayalam Movie names   ")
    print("-----------------------------------")
    print("Instructions:")
    print("1. Player 1 enters the movie name (while Player 2 looks away).")
    print("2. Player 2 tries to guess the movie letter by letter.")
    print("3. You have a limited number of incorrect chances.")
    print("Thank You, Enjoy!\n")

    countdown()
    secret_movie = input("Player 1, enter the Movie name: ").lower()
    print("\n" * 50)
    print("Player 2, it's your turn to guess!")

    display = []
    for char in secret_movie:
        if char == " ":
            display.append(" ")
        else:
            display.append("_")

    chances = 5
    guessed_letters = []

    while chances > 0 and "_" in display:
        print("\n" + " ".join(display))
        print(f"You have {chances} chances left.")

        guess = input("Enter your alphabet: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid alphabet letter.")
            continue

        if guess in guessed_letters:
            print(f"You already guessed the letter '{guess}'. Try a different one.")
            continue

        guessed_letters.append(guess)

        if guess in secret_movie:
            print(f"Good job! '{guess}' is in the movie.")
            for index, char in enumerate(secret_movie):
                if char == guess:
                    display[index] = guess
        else:
            chances -= 1
            print(f"Wrong guess! '{guess}' is not in the movie.")

    print("\n-----------------------------------")
    if "_" not in display:
        print(" ".join(display))
        print("Congratulations! You guessed the movie correctly! 🎉")
    else:
        print(f"Game Over! The correct movie was: '{secret_movie}'. Better luck next time! 😢")
    print("-----------------------------------")

if __name__ == "__main__":
    hangman_game()







