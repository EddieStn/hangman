from words import word_list
import random
import time

word = random.choice(word_list)

def greeting():
    """
    Welcomes the player into the game
    """
    print("Welcome to hangman!")
    time.sleep(0.5)
    player = input("Choose a nickname:")
    time.sleep(0.5)
    print(f"Hello, {player}, the game starts now!")
    time.sleep(1)
    print("Good luck!")
    time.sleep(1)


greeting()

def display_hangman(attempt):
    """
    Display the different levels of hangman based of number of failures
    """
    if attempt == 0:
        print("""
            +---+
            |   |
            |
            |
            |
            ______""")
    elif attempt == 1:
        print("""
            +---+
            |   |
            |   O
            |
            |
            ______""")
    elif attempt == 2:
        print("""
            +---+
            |   |
            |   O
            |   |
            |
            ______""")    
    elif attempt == 3:
        print("""
            +---+
            |   |
            |   O
            |  /|
            |
            ______""") 
    elif attempt == 4:
        print("""
            +---+
            |   |
            |   O
            |  /|\\
            |
            ______""") 
    elif attempt == 5:
        print("""
            +---+
            |   |
            |   O
            |  /|\\
            |  /
            ______""") 
    elif attempt == 6:
        print("""
            +---+
            |   |
            |   O
            |  /|\\
            |  / \\
            ______""") 
    return attempt


attempt = display_hangman(0)



def check_guess():
    """
    Check whether player`s input is a letter or not
    """
    global attempt
    
    while attempt <= 6:
        attempt = 0
        print("The word is:")
        hidden_word = "_" * len(word)
        print(hidden_word)
        guess = input("Guess a letter: ")
        guess = guess.upper()
        for letter in guess:
            if letter.isalpha():
                if len(letter) > 1:
                    print("You can only choose one letter")
            else:
                print("Not a letter, try again.")
        if guess in word:
            print(f"That is correct, {guess} is in the word")
        else:
            attempt += 1
            print(f"{guess} is not in the word. attempts left: {attempt}")
    

check_guess()
    