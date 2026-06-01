'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
import random

words = ["apple", "mango", "tiger", "table", "river"]

secret_word = random.choice(words)

guessed_letters = []
wrong_count = 0

print("Welcome to Hangman Game")

while wrong_count < 6:

    display = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display = display + letter + " "
        else:
            display = display + "_ "

    print("\nWord:", display)

    if "_" not in display:
        print("Congratulations! You guessed the word.")
        break

    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed this letter.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("Correct Guess!")
    else:
        wrong_count = wrong_count + 1
        print("Wrong Guess!")
        print("Remaining Chances:", 6 - wrong_count)

if wrong_count == 6:
    print("\nGame Over!")
    print("The word was:", secret_word)