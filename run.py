"""
Hangman game using functions, if and while loops,
try blocks, handles user input and uses time.sleep()
for better user experience
"""


import random
import time
from assets import word_list
from assets import display_hangman


# \n after every input?
# requirements empty


def get_word():
    """
    Get a random word form the word list
    """
    word = random.choice(word_list)
    return word.upper()


def greeting():
    """
    Welcomes the player into the game and brings up the menu()
    which starts the game or shows the rules
    """
    print("Welcome to hangman!")
    time.sleep(0.5)
    player = input("Choose a nickname:\n")
    time.sleep(0.5)
    print(f"Hello, {player}, See the menu before we start the game")
    time.sleep(1)
    menu()
    time.sleep(1)


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
    word = get_word()
    hidden_word = "_" * len(word)
    guessed_letters = []
    guessed_words = []
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


def menu():
    """
    Prompts the user with a choice to see the rules before playing
    and also starts the game should they wish to play
    """
    word = get_word()
    while True:
        try:
            choice = input(
                "For instructions type 'RULES', to start game type 'PLAY':\n")
            choice = choice.lower()
            if choice == "play":
                time.sleep(1)
                hangman(word)
            elif choice == "rules":
                print("\n- Hangman is a puzzle game\n")
                time.sleep(1)
                print("- Your goal is to guess the secret word\n")
                time.sleep(1)
                print(
                    "- You can guess one letter at a time or the whole word\n")
                time.sleep(1)
                print("- You've only got 6 wrong attempts before you hang\n")
                time.sleep(1)
                print("- That been said, good luck and have fun!\n")
                time.sleep(1)
                start = input("Start playing? (Y - yes / N - no): \n")
                while start not in ["y", "n", "Y", "N"]:
                    start = input("Start playing? (Y for yes / N for no): \n")
                if start == "y":
                    time.sleep(1)
                    hangman(word)
                elif start == "n":
                    print("\nThat`s a shame, maybe some other time.")
            else:
                raise ValueError("That is not a valid input")
            break
        except ValueError as v_e:
            print(v_e)


def play_loop():
    """
    Game loop, asks the user if they want to play again
    and if so it restarts the game
    """
    word = get_word()
    play_again = input("Play Again? (Y/N):\n")
    while play_again not in ["y", "n", "Y", "N"]:
        play_again = input("Play Again? (Y for yes / N for no):\n")
    if play_again == "y":
        time.sleep(1)
        hangman(word)
    elif play_again == "n":
        time.sleep(0.5)
        print("Thank you for playing.")
        time.sleep(0.5)
        print("See you next time!")


greeting()
