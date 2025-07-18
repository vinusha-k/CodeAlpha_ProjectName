# CodeAlpha_ProjectName

import random

def hangman():
    words = ["apple", "banana", "grape", "mango", "peach"]
    word = random.choice(words)
    guessed = ["_"] * len(word)
    attempts = 6
    guessed_letters = []

    print("Welcome to Hangman!")

    while attempts > 0 and "_" in guessed:
        print("\nWord:", " ".join(guessed))
        print("Attempts left:", attempts)
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed[i] = guess
            print("Good guess!")
        else:
            attempts -= 1
            print("Wrong guess!")
        guessed_letters.append(guess)

    if "_" not in guessed:
        print("\nCongratulations! You guessed the word:", word)
    else:
        print("\nGame over! The word was:", word)

if __name__ == "__main__":
    hangman()