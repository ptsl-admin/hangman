from hangman import HangMan

hangman = HangMan()


def prompt_continue_play():
    play_next = str(input("Play next round (y for yes): ")).lower().strip()  # ask if user want to play next round

    if play_next.lower() == 'y':
        hangman.start_game()  # start new game, since new game is started hangman.is_game_over() returns false and
        print("Guess the following word:")
        print(hangman.get_hang_word())
        return True
        # hence the loop continues
    return False


# setting
hangman.set_max_guess(12)
hangman.set_hang_char("_")

# start game (round)
hangman.start_game()

# guess the word
print("Guess the following word:")
print(hangman.get_hang_word())

continue_play = True  # by default play is continued
while continue_play:
    guess_character = str(input("\nEnter a Guess Character (Or, enter 0 to give up): "))

    if guess_character == "0":
        hangman.give_up()  # give up current game

        continue_play = prompt_continue_play()  # get response from user if s/he wants to continue to play

        continue

    response = hangman.make_guess(guess_character)

    print(hangman.get_hang_word())

    hangman.display_stat(response)

    if hangman.is_game_over():
        continue_play = prompt_continue_play()

# display all rounds played
print("\n\n" * 5)
print("Game History:")
print("-" * 20)
print(hangman.get_game_rounds())
