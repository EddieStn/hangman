from words import word_list
import random


def get_word():
    """
    Get a random word from the word list
    """
    word = random.choice(word_list)
    return word.upper()


