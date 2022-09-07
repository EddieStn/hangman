"""
Provide a list of words from which the main program
could pick a random one.
Home for the display_hangman function which is used
in the main program to save clatter
"""


word_list = ["jury", "attitude", "queue", "moving", "momentum",
             "lighter", "conservative", "command", "inappropriate",
             "memorandum", "stool", "snow", "relaxation", "constituency",
             "learn", "equinox", "nursery", "structure", "argument",
             "species", "basketball", "few", "parade", "mushroom",
             "speech", "squeeze", "ton", "cycle", "diameter", "auditor"]


def display_hangman(fails):
    """
    Display the different stages of hangman based on number of failures
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
