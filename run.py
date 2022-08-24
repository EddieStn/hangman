import random
from word_list import words


def get_word():
    """
    Get a random word from the word list
    """
    word = random.choice(words)
    return word.upper()


