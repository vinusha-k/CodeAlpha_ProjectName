import random

words = ["apple", "banana", "grape", "mango", "peach"]
word = random.choice(words)
guessed = "_" * len(word)
attempts = 6

print("Welcome to Hangman!")

while attempts > 0 and "_" in guessed:
    print("\nWord:", " ".join(guessed))
    print("Attempts left:", attempts)
    guess = input("Guess a letter: ")

    if guess in word:
        new = ""
        for i in range(len(word)):
            if word[i] == guess:
                new += guess
            else:
                new += guessed[i]
        guessed = new
        print("Correct!")
    else:
        attempts -= 1
        print("Wrong!")

if "_" not in guessed:
    print("\nYou won! The word was:", word)
else:
    print("\nYou lost! The word was:", word)