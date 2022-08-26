from words import word_list
import random


def get_word():
    """
    Get a random word from the word list
    """
    random_word = random.choice(word_list)
    return random_word.upper()


word = get_word()
print(word)



def display_hangman(attempt):
    """
    Display the hangman building up on wrong choices
    """
    if attempt == 0:
        print("""
            +---+
            |
            |
            |
            ______""")
    elif attempt == 1:
        print("""
            +---+
            |   O
            |
            |
            ______""")
    elif attempt == 2:
        print("""
            +---+
            |   O
            |   |
            |
            ______""")    
    elif attempt == 3:
        print("""
            +---+
            |   O
            |  /|
            |
            ______""") 
    elif attempt == 4:
        print("""
            +---+
            |   O
            |  /|\\
            |
            ______""") 
    elif attempt == 5:
        print("""
            +---+
            |   O
            |  /|\\
            |  /
            ______""") 
    elif attempt == 6:
        print("""
            +---+
            |   O
            |  /|\\
            |  / \\
            ______""") 
    return attempt


attempt = display_hangman(0)


while attempt <= 6:
    def check_guess():
        """
        Check whether player`s input is a letter or not
        """
        global attempt
        guess = input("Guess a letter: ")
        for letter in guess:
            if letter.isalpha():
                print(f"You picked: {guess}")
            else:
                print("Not a letter")
        if guess in word:
            print(f"That is correct, {guess} is in the word")
        else:
            attempt += 1
            print(f"{guess} is not in the word. attempts left: {attempt}")
            

check_guess()
    