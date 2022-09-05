import random
import time
from words import word_list

# \n after every input?


def get_word():
    """
    Get a random word form the word list
    """
    word = random.choice(word_list)
    return word.upper()


# menu, play / instructions (rules)


def greeting():
    """
    Welcomes the player into the game
    """
    print("Welcome to hangman!")
    time.sleep(0.5)
    player = input("Choose a nickname:\n")
    time.sleep(0.5)
    print(f"Hello, {player}, the game starts now!")
    time.sleep(1)
    print("Good luck!")
    time.sleep(1)


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


def play_loop():
    """
    Game loop, asks the user if they want to play again
    """
    play_again = input("Play Again? (Y/N):\n")
    while play_again not in ["y", "n", "Y", "N"]:
        play_again = input("Play Again? (Y for yes / N for no):\n")
    if play_again == "y":
        hangman(word)
    elif play_again == "n":
        time.sleep(0.5)
        print("Thank you for playing.")
        time.sleep(0.5)
        print("See you next time!")


# def check_guess(word):
#     """
#     Check whether player`s input is a letter or not
#     """
#     guessed_letters = []
#     while True:
#         guess = input("Guess a letter: ").upper()
#         if guess.isalpha() and len(guess) == 1:
#             if guess in guessed_letters:
#                 print(f"You already guessed: {guess} ")
#             elif guess not in word:
#                 print(f"{guess} is not in the word.")
#                 guessed_letters.append(guess)
#         else:
#             print(f"{guess} Invalid. Try one letter")
#     return guess


def hangman(word):
    """
    The main loop that checks if user input is valid
    and whether it`s in the word
    """
    guessed_letters = []
    guessed_words = []
    hidden_word = "_" * len(word)
    fails = 0
    guessed = False
    print(display_hangman(fails))
    print(f"The word is: \n{hidden_word}\n")
    while not guessed and fails < 6:
        guess = input("Please guess a letter or word:\n").upper()
        if guess.isalpha() and len(guess) == 1:
            if guess in guessed_letters:
                print(f"You already guessed the letter: {guess}")
            elif guess not in word:
                print(f"{guess} is not in the word.")
                fails += 1
                guessed_letters.append(guess)
            else:
                print(f"Good job! {guess} is in the word.")
                guessed_letters.append(guess)
                word_as_list = list(hidden_word)
                indices = [i for i, letter in enumerate(
                    word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                hidden_word = "".join(word_as_list)
                if "_" not in hidden_word:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                fails += 1
                guessed_words.append(guess)
            else:
                guessed = True
                hidden_word = word
        else:
            print(f"{guess} Invalid. Try one letter")
        print(display_hangman(fails))
        print(hidden_word)
        print("\n")
    if guessed:
        print("WEll DONE! You guessed the word!\n")
        time.sleep(1)
        play_loop()
    else:
        print(f"You got hanged! Better luck next time. The word was {word}\n")
        time.sleep(1)
        play_loop()


greeting()
word = get_word()
hangman(word)


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
