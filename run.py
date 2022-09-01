from words import word_list
import random
import time


def get_word():
    """
    Get a random word form the word list
    """
    word = random.choice(word_list)
    return word.upper()


word = get_word()


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


# def game_mode():
#     mode = input("Choose game mode (EASY/HARD): ")
#     max_fails = stages
#     if mode != "EASY" and mode != "HARD":
#         print("Invalid input, try EASY/HARD")
#     elif mode == "easy":
#         max_fails = stages
#         print("You chose EASY, you get 6 attempts")
#     else:
#         max_fails = stages[1:-1:2]
#         print("You chose HARD, you get 3 attempts")
#     return mode.upper()


def check_guess(word):
    """
    Check whether player`s input is a letter or not
    """
    guessed_letters = []
    fails = 0
    while True:
        guess = input("Guess a letter: ").upper()
        if guess.isalpha() and len(guess) == 1:
            if guess in guessed_letters:
                print(f"You already guessed: {guess} ")
            elif guess not in word:
                print(f"{guess} is not in the word.")
                fails += 1
                guessed_letters.append(guess)
        else:
            print(f"{guess} Invalid. Try one letter")


check_guess(word)


def display_hangman(fails):
    """
    Display the different stages of hangman based of number of failures
    """
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
    return stages[fails]


# def get_mode():
#     """
#     Prompt the user to choose game mode
#     """
#     global stages
#     while True:
#         try:
#             mode = input("Choose game mode (EASY/HARD): ")
#             mode = mode.upper()
#             if mode == 'easy':
#                 print("You chose EASY")
#                 return stages
#             elif mode == 'hard':
#                 print("You chose HARD")
#                 stages = stages[1:-1:2]
#                 return stages
#             else:
#                 return stages
#         except ValueError():
#             if mode != "easy" and mode != "hard":
#                 print("Invalid input, choose EASY/HARD")
#         return


# get_mode()


# while attempt <= 6:
#     attempt = 0
#     print("The word is:")
#     hidden_word = "_" * len(word)
#     print(hidden_word)
