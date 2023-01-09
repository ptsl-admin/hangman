import random as rd


class HangMan:
    __words = []
    __GAME_MODE = 0  # 0 represents no game is happening, 1 represents game is ongoing
    DEFAULT_MAX_GUESS = 12
    __HANG_CHAR = "-"  # default hang character
    __CORRECT_GUESS_MSG = [
        "Nice work! Keep going",
        "Excellent job, keep it coming",
        "Hmm... You are a fast learner! Stay with that",
        "You're so good at this !!! Carry on",
        "How did you do this so fast? Continue like this",
        "Terrific job, Stick it out",
        "This is insanely good! Press on"
    ]
    __WRONG_GUESS_MSG = [
        "You're on the right track, but not there yet",
        "Come on try harder!! You can do it",
        "You have almost made. Just don not give up!!",
        "Come on! You can do it!",
        "Wait, you can do the impossible, Just Keep Fighting! "
    ]

    __CONGRATULATION_MSG = [
        "Congratulations! The system is so very proud of you!",
        "Your smart guess and perseverance have paid off. Congratulations!",
        "Congratulations on your well-deserved success! You’re an inspiration!",
        "Enjoy your new success. Congratulations!",
        "You got what you deserved. Congratulations!!",
        "You have climbed the top. Well Done!!",
        "You are the CHAMPION! Your legend grows with this win.",
        "Your performance was stunning! You are the best."
    ]

    def __init__(self):
        self.__GUESSED_CHARS = []
        self.__CURRENT_GUESS_COUNT = None
        self.__WORD_TO_GUESS = ""
        self.__max_guess = self.DEFAULT_MAX_GUESS
        self.__load_dictionary()
        self.__ROUNDS = []  # records each game round information

    def __load_dictionary(self):
        with open("words.txt", "r") as f:
            for x in f:
                if len(x) > 3:
                    self.__words.append(x.strip())

    def __get_random_word(self):
        return self.__words[rd.randint(0, len(self.__words))]

    def set_hang_char(self, char):
        self.__HANG_CHAR = char[0]  # just accept one character only

    def get_hang_char(self):
        return self.__HANG_CHAR

    def set_max_guess(self, guess: int = 5):
        if self.__GAME_MODE == 0:
            self.__max_guess = guess

    def get_max_guess(self):
        return self.__max_guess

    def start_game(self):
        if self.__GAME_MODE == 1:  # there is nothing to do if game is ongoing
            return False

        # update game mode
        self.__GAME_MODE = 1
        self.__WORD_TO_GUESS = self.__get_random_word()
        self.__GUESSED_CHARS = []
        self.__CURRENT_GUESS_COUNT = len(self.__GUESSED_CHARS)

        # update round information
        self.__update_round()

        return True

    def make_guess(self, char):
        if self.__GAME_MODE == 0:
            return {"success": 0, "msg": "Game has not been started. Please start the game first", "guess_count": 0}

        char = char[0]  # just accept one character from the string
        if char in self.__GUESSED_CHARS:
            return {"success": 0, "msg": "You already guessed this character. Please make a different guess.",
                    "guess_count": self.__CURRENT_GUESS_COUNT}

            # add char letter to guessed chars list
        self.__GUESSED_CHARS.append(char)  # only the first character will be taken into consideration

        # update current guess count
        self.__CURRENT_GUESS_COUNT = len(self.__GUESSED_CHARS)

        # see if all guessed chars are in the current word (WORD TO GUESS)
        temp = self.__WORD_TO_GUESS
        for char in self.__GUESSED_CHARS:
            if char in temp:
                temp = temp.replace(char, '')
        if len(temp) == 0:
            # we can conclude that user has successfully made a guess
            self.__GAME_MODE = 0  # since user won, this game (round) is over

            msg = self.__CONGRATULATION_MSG[rd.randint(0, len(self.__CONGRATULATION_MSG) - 1)]
            response = {"success": 1, "msg": msg, "guess_count": self.__CURRENT_GUESS_COUNT}
            self.__update_round(response)
            return response

        if self.__CURRENT_GUESS_COUNT >= self.get_max_guess():
            self.__GAME_MODE = 0  # since user lost, this game (round) is over
            response = {"success": 0, "msg": "You Loose!! The word was " + self.__WORD_TO_GUESS,
                        "guess_count": self.__CURRENT_GUESS_COUNT}
            self.__update_round(response)
            return response

        # detect if current guess char was correct and msg accordingly
        if char in self.__WORD_TO_GUESS:
            msg = self.__CORRECT_GUESS_MSG[rd.randint(0, len(self.__CORRECT_GUESS_MSG) - 1)]
            response = {"success": 2, "msg": msg, "guess_count": self.__CURRENT_GUESS_COUNT}
            # success 2 means that the current guess was correct
            return response

            # just in case, throw this response
        msg = self.__WRONG_GUESS_MSG[rd.randint(0, len(self.__WRONG_GUESS_MSG) - 1)]
        return {"success": 0, "msg": msg, "guess_count": self.__CURRENT_GUESS_COUNT}

    def get_hang_word(self):
        if len(self.__WORD_TO_GUESS) == 0:
            # if there was no last guessed chars then we show default hang word
            return (" " + self.__HANG_CHAR + " ") * self.DEFAULT_MAX_GUESS

        hang_word = ""
        for char in self.__WORD_TO_GUESS:
            if char in self.__GUESSED_CHARS:
                hang_word += " " + str(char).upper() + " "
            else:
                hang_word += " " + self.get_hang_char() + " "

        return hang_word

    def is_game_over(self):
        if self.__GAME_MODE == 0:
            return True

        if self.__CURRENT_GUESS_COUNT >= self.get_max_guess():
            return True

        return False

    def display_stat(self, response):
        print("\nMessage: " + response["msg"])
        print("Guess: {0} \t | Guess left : {1} \t | Guessed Letters : \t {2} ".format(
            response["guess_count"],
            self.get_max_guess() - response["guess_count"],
            ",".join(self.__GUESSED_CHARS)
        ))
        print("\n")

    def get_guessed_chars(self):
        # returns all guessed characters for this round
        return self.__GUESSED_CHARS

    def __update_round(self, response=None):

        if isinstance(response, dict):
            self.__ROUNDS.append({
                "word": self.__WORD_TO_GUESS,
                "status": response["success"],  # 0 means lost 1 means won 3 means gave up
                "guessed_chars": self.__GUESSED_CHARS
            })

        # update wins        
        self.__WINS = 0
        for rounds in self.__ROUNDS:
            if rounds["status"] == 1:
                self.__WINS += 1

        # update total rounds
        self.__TOTAL_ROUNDS = len(self.__ROUNDS)

        # update win rate
        if self.__TOTAL_ROUNDS == 0:
            self.__WIN_RATE = 0
        else:
            self.__WIN_RATE = int(self.__WINS / self.__TOTAL_ROUNDS * 100)

    def get_game_rounds(self):
        return self.__ROUNDS

    def get_round_status(self):
        return {
            "rounds": self.__TOTAL_ROUNDS,
            "wins": self.__WINS,
            "win_rate": self.__WIN_RATE
        }

    def give_up(self):
        if self.__GAME_MODE == 0:
            return {"success": 0, "msg": "There is no ongoing game"}

        msg = "You gave up!! The word was : " + self.__WORD_TO_GUESS
        response = {"success": 3, "msg": msg, "guess_count": self.__CURRENT_GUESS_COUNT}
        self.__update_round(response)

        # update game mode
        self.__GAME_MODE = 0  # since user gave up this round, change game mode to 0
        return {"success": 1, "msg": msg}
