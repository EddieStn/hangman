from words import word_list
import random
import time


def get_word():
    """
    Get a random word form the word list
    """
    word = random.choice(word_list)
    return word.upper()

# menu, play / instructions (rules)
# play again?
# already guessed
# guess word?


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


# greeting()


def game_mode():
    mode = input("Choose game mode (EASY/HARD): ")
    max_fails = stages
    if mode != "EASY" and mode != "HARD":
        print("Invalid input, try EASY/HARD")
    elif mode == "easy":
        max_fails = stages
        print("You chose EASY, you get 6 attempts")
    else:
        max_fails = stages[1:-1:2]
        print("You chose HARD, you get 3 attempts")
    return mode.upper()


def check_guess():
    """
    Check whether player`s input is a letter or not
    """
    while True:
        guess = input("Guess a letter: ")
        guess = guess.upper()
        if guess.isalpha() and len(guess) == 1:
            print(f"{guess} is Valid")
        else:
            print(f"{guess} Invalid. Try one letter")


# check_guess()


# Change function to array of stages so max_fails
# can get a different number of stages by indexing

stages = [
    """
    +---+
    |   |
    |
    |
    |
    ______
    """,
    """
    +---+
    |   |
    |   O
    |
    |
    ______
    """,
    """
    +---+
    |   |
    |   O
    |   |
    |
    ______
    """,
    """
    +---+
    |   |
    |   O
    |  /|
    |
    ______
    """,
    """
    +---+
    |   |
    |   O
    |  /|\\
    |
    ______
    """,
    """
    +---+
    |   |
    |   O
    |  /|\\
    |  /
    ______
    """,
    """
    +---+
    |   |
    |   O
    |  /|\\
    |  / \\
    ______
    """
]


def get_mode():
    """
    Prompt the user to choose game mode
    """
    global stages
    try:
        difficulty = input("Choose game mode (EASY/HARD): ")
        difficulty = difficulty.upper()
        if difficulty == 'easy':
            print("You chose EASY")
            return stages
        elif difficulty == 'hard':
            print("You chose HARD")
            stages = stages[1:-1:2]
            return stages
        else:
            return stages
    except ValueError():
        if difficulty != "easy" and difficulty != "hard":
            print("Invalid input, choose EASY/HARD")
    return


get_mode()


# while attempt <= 6:
#     attempt = 0
#     print("The word is:")
#     hidden_word = "_" * len(word)
#     print(hidden_word)


# def display_hangman(attempt):
#     """
#     Display the different stages of hangman based of number of failures
#     """
#     if attempt == 0:
#         print("""
#             +---+
#             |   |
#             |
#             |
#             |
#             ______""")
#     elif attempt == 1:
#         print("""
#             +---+
#             |   |
#             |   O
#             |
#             |
#             ______""")
#     elif attempt == 2:
#         print("""
#             +---+
#             |   |
#             |   O
#             |   |
#             |
#             ______""")  
#     elif attempt == 3:
#         print("""
#             +---+
#             |   |
#             |   O
#             |  /|
#             |
#             ______""")
#     elif attempt == 4:
#         print("""
#             +---+
#             |   |
#             |   O
#             |  /|\\
#             |
#             ______""")
#     elif attempt == 5:
#         print("""
#             +---+
#             |   |
#             |   O
#             |  /|\\
#             |  /
#             ______""")
#     elif attempt == 6:
#         print("""
#             +---+
#             |   |
#             |   O
#             |  /|\\
#             |  / \\
#             ______""")
#     return attempt
