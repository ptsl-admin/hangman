from hangman import HangMan
from time import sleep
from hangman_gui import App

hangman = HangMan()


if __name__ == "__main__":
    
    app = App(hangman)

