# Hangman

[Live link](https://hangman25.herokuapp.com/)

This is a simple hangman game project, built with python, deployed on Heroku and is strictly terminal-based for user interaction.
This project is designed for people who love puzzles, maybe bringing them back childhood memories, even tho it being somehow offensive, it's just a fun, thinking game.
And hangman is a word-guessing puzzle where you are given a secret word, knowing only the length of it by underscores. And by guessing out some letters, try to figure out the secret word before the man hangs, when each wrong attempt adds a part of the man's body to the gallows.

# Features

# Technology 

* Python
* Heroku
* Github
* Gitpod

## Libraries 

* Random
* Os
* Time

# User stories

* I want to see a fresh screen after a guess
    * Created a function to clear the terminal after each guess and when a new game begins
* I want to be able to see game instructions
    * Created the menu function which gives user the choice to either play or see the rules before playing
* I want to see the already guessed letters
    * Printed the already_guessed letters list for the user before new guess input

# Testing

Testing for this project has been done manually and thoroughly by me and some people that I asked to try it out, trying to break the code in every possible way, but failed. All feedback received was positive and no errors encountered when playing, other than not guessing the word :). However, it does not work on mobile.

## Code validation

No errors found when running the code through pep8 online checker. Same for both assets.py and run.py

<img src="assets/pep8.png" alt="code validator pep8" width="600">

# Bugs

* The underscores on Heroku did not have any spacing between them
* only white spaces would work for the name input > at first created a function to check for valid_input but then I made it redundant because I found a simpler approach using a while loop

```
def valid_input(text):
    """
    Checks that the user input doesn`t have only blank spaces
    """
    not_valid = True
    result = ''
    while not_valid:
        result = input(text)
        print("You can`t have an empty nickname...")
        if result.split():
            not_valid = False
    return result
```
```
player = input("Choose a nickname:\n")
    while not player.strip():
        print("You can`t have an empty nickname...")
        player = input("Choose a nickname:\n")
```

# Local Development

## Forking and Cloning

## Forking a repository
### A fork is a copy of a repository. Forking a repository allows you to freely experiment with changes without affecting the original project.
1. On GitHub.com, navigate to the EddieStn/hangman repository.
2. In the top-right corner of the page, click Fork.

## Cloning your forked repository
### Right now, you have a fork of the hangman repository, but you do not have the files in that repository locally on your computer.
1. On GitHub.com, navigate to your fork of the hangman repository.
2. Above the list of files, click Code.
3. Copy the URL for the repository.
4. Open Git Bash.
5. Change the current working directory to the location where you want the cloned directory.
6. Type git clone, and then paste the URL you copied earlier. It will look like this, with your GitHub username instead of YOUR-USERNAME:
   - git clone https://github.com/YOUR-USERNAME/hangman
7. Press Enter. Your local clone will be created.
8. Requirements.txt can be left empty as this project does not use any external libraries.

# Deployment
### The site was deployed to Heroku. The steps to deploy are as follows:


* Log in to Heroku Heroku
* Click New
* Give the app a name and choose the region
* Click on settings first and set the Reveal Config Vars
* Key = PORT, Value = 8000
* Add python and nodeJs as buildpacks, making sure that python is on top
* Click Deploy at the top to go to the Deployment settings
* Choose GitHub as the deployment method
* Search for your app and connect
* Use Automatic deploys if you would like a new build when changes are pushed to GitHub from Gitpod
* Use Manual deploy for a new build every time this button is clicked.
* Once completed click View App.

The live link can be found here - (https://hangman25.herokuapp.com/)

# Credits

[Hangman tutorial](https://github.com/kiteco/python-youtube-code/blob/master/build-hangman-in-python/hangman.py) - this project tutorial helped me find a solution to a issue i had, using enumerate to swap each "_" to the guessed letter.
# Acknowledgements

* Many thanks to Chris Quinn, my mentor, for guidance and for his brilliant ideas

## Websites that thought me python

* [code with mosh](https://codewithmosh.com/)
* 
