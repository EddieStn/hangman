from words import word_list
import random


def get_word():
    """
    Get a random word from the word list
    """
    word = random.choice(word_list)
    return word.upper()

def display_hangman(attempts):
    if attempts == 0:
        print("""
            +---+
            |
            |
            |
            ______""")
    elif attempts == 1:
        print("""
            +---+
            |   O
            |
            |
            ______""")
    elif attempts == 2:
        print("""
            +---+
            |   O
            |   |
            |
            ______""")    
    elif attempts == 3:
        print("""
            +---+
            |   O
            |  /|
            |
            ______""") 
    elif attempts == 4:
        print("""
            +---+
            |   O
            |  /|\\
            |
            ______""") 
    elif attempts == 5:
        print("""
            +---+
            |   O
            |  /|\\
            |  /
            ______""") 
    elif attempts == 6:
        print("""
            +---+
            |   O
            |  /|\\
            |  / \\
            ______""") 


display_hangman(6)

    