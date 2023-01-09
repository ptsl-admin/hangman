import tkinter as tk
from tkinter import messagebox as msgbox
from tkinter import simpledialog as inputbox
import tkinter.font as tkFont
from time import sleep

class App:
    
    def __init__(self, hangman):
        self.hm = hangman
        
        self.__root = root = tk.Tk()
        self.__load_elements()
        self.__root.mainloop()
        
    def __load_elements(self):
        # get the root
        root = self.__root
        
        #setting title
        root.title("Hang Man")
        #setting window size
        width=684
        height=291
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        self.lbl_hang_word=tk.Label(root)        
        self.lbl_hang_word["borderwidth"] = "2px"
        self.lbl_hang_word["cursor"] = "star"
        ft = tkFont.Font(family='Times',size=36)
        self.lbl_hang_word["font"] = ft
        self.lbl_hang_word["fg"] = "#999999"
        self.lbl_hang_word["justify"] = "center"
        self.lbl_hang_word["text"] = self.hm.get_hang_word()
        self.lbl_hang_word["relief"] = "raised"
        self.lbl_hang_word.place(x=0,y=100,width=684,height=60)        

        self.lbl_game_round=tk.Label(root)
        self.lbl_game_round["cursor"] = "arrow"
        ft = tkFont.Font(family='Times',size=22)
        self.lbl_game_round["font"] = ft
        self.lbl_game_round["fg"] = "#1e9fff"
        self.lbl_game_round["justify"] = "left"
        self.lbl_game_round["text"] = "Game : "
        self.lbl_game_round["relief"] = "groove"
        self.lbl_game_round.place(x=10,y=10,width=135,height=35)

        self.lbl_game_wins=tk.Label(root)        
        self.lbl_game_wins["cursor"] = "arrow"
        ft = tkFont.Font(family='Times',size=22)
        self.lbl_game_wins["font"] = ft
        self.lbl_game_wins["fg"] = "#1e9fff"
        self.lbl_game_wins["justify"] = "left"
        self.lbl_game_wins["text"] = "Wins : "
        self.lbl_game_wins["relief"] = "groove"
        self.lbl_game_wins.place(x=250,y=10,width=125,height=35)

        # label guess count
        self.lbl_guess_count=tk.Label(root)        
        self.lbl_guess_count["cursor"] = "arrow"
        ft = tkFont.Font(family='Times',size=18)
        self.lbl_guess_count["font"] = ft
        self.lbl_guess_count["fg"] = "#1e9fff"
        self.lbl_guess_count["justify"] = "left"
        self.lbl_guess_count["text"] = "Guess : "
        self.lbl_guess_count["relief"] = "groove"
        #self.lbl_guess_count.place(x=10,y=120,width=125,height=35)
        

        # label guessed characters
        self.lbl_guess_chars=tk.Label(root)        
        self.lbl_guess_chars["cursor"] = "arrow"
        ft = tkFont.Font(family='Times',size=18)
        self.lbl_guess_chars["font"] = ft
        self.lbl_guess_chars["fg"] = "#1e9fff"
        self.lbl_guess_chars["anchor"] = "w"
        self.lbl_guess_chars["text"] = "Guesses : "
        self.lbl_guess_chars["relief"] = "groove"
        #self.lbl_guess_chars.place(x=135,y=120,width=540,height=35)         

        self.lbl_game_win_rate=tk.Label(root)
        self.lbl_game_win_rate["cursor"] = "arrow"
        ft = tkFont.Font(family='Times',size=22)
        self.lbl_game_win_rate["font"] = ft
        self.lbl_game_win_rate["fg"] = "#1e9fff"
        self.lbl_game_win_rate["justify"] = "left"
        self.lbl_game_win_rate["text"] = "Win Rate :"
        self.lbl_game_win_rate["relief"] = "groove"
        self.lbl_game_win_rate.place(x=480,y=10,width=195,height=35)

        # make guess button
        self.btn_make_guess=tk.Button(root)
        self.btn_make_guess["bg"] = "#f0f0f0"
        self.btn_make_guess["cursor"] = "arrow"
        ft = tkFont.Font(family='Times',size=12)
        self.btn_make_guess["font"] = ft
        self.btn_make_guess["fg"] = "#000000"
        self.btn_make_guess["justify"] = "center"
        self.btn_make_guess["text"] = "⚄ Guess"
        #self.btn_make_guess.place(x=135,y=165,width=120,height=30)
        self.btn_make_guess["command"] = self.btn_make_guess_command        

        self.btn_start=tk.Button(root)
        self.btn_start["bg"] = "#f0f0f0"
        self.btn_start["cursor"] = "arrow"
        ft = tkFont.Font(family='Times',size=12)
        self.btn_start["font"] = ft
        self.btn_start["fg"] = "#000000"
        self.btn_start["justify"] = "center"
        self.btn_start["text"] = "▷ Start Game"
        self.btn_start.place(x=30,y=240,width=120,height=30)
        self.btn_start["command"] = self.btn_start_command

        # the give up button
        self.btn_give_up=tk.Button(root)
        self.btn_give_up["bg"] = "#f0f0f0"
        self.btn_give_up["cursor"] = "arrow"
        ft = tkFont.Font(family='Times',size=12)
        self.btn_give_up["font"] = ft
        self.btn_give_up["fg"] = "#000000"
        self.btn_give_up["justify"] = "center"
        self.btn_give_up["text"] = "⏹ Give Up"
        self.btn_give_up.place(x=200,y=240,width=120,height=30)
        self.btn_give_up["command"] = self.btn_give_up_command
        self.btn_give_up["state"] = "disabled" #  by default user cannot give coz game will not have started

        self.btn_setting=tk.Button(root)
        self.btn_setting["bg"] = "#f0f0f0"
        self.btn_setting["cursor"] = "arrow"
        ft = tkFont.Font(family='Times',size=12)
        self.btn_setting["font"] = ft
        self.btn_setting["fg"] = "#000000"
        self.btn_setting["justify"] = "center"
        self.btn_setting["text"] = "⚙ Setting "
        self.btn_setting.place(x=370,y=240,width=120,height=30)
        self.btn_setting["command"] = self.btn_setting_command

        # button game history
        self.btn_game_history = tk.Button(root)
        self.btn_game_history["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=12)
        self.btn_game_history["font"] = ft
        self.btn_game_history["fg"] = "#000000"
        self.btn_game_history["justify"] = "center"
        self.btn_game_history["text"] = "Played Words"
        self.btn_game_history.place(x=540,y=240,width=120,height=30)
        self.btn_game_history["command"] = self.btn_game_history_command        

    def btn_give_up_command(self):
        print("Giving Up...")

        print(self.hm.give_up())
        
        print(self.hm.is_game_over())
        if self.hm.is_game_over():
            self.__restore_game_over_state()        


    
    def btn_start_command(self):
        started = self.hm.start_game()
        if not started:
            self.display_warning("Error", "Could not start game.")
        else:
            self.display_info("Game Started", "Good Luck!")

        # update lbl hang word
        self.lbl_hang_word["fg"] = "#000000"
        self.lbl_hang_word.configure(text=self.hm.get_hang_word())
        self.lbl_hang_word.place(x=0,y=50,width=684,height=60) 

        # disable start button
        self.btn_start["state"] = "disabled"

        # disable setting button
        self.btn_setting["state"] = "disabled"

        # enable give up buttton
        self.btn_give_up["state"] = "normal"        

        # get round status from hangman class
        round_status = self.hm.get_round_status()
        
        # update game count (round) label
        self.lbl_game_round["text"] = "Game : " + str(round_status["rounds"] + 1)

        # update game wins label
        self.lbl_game_wins["text"] = "Wins : " + str(round_status["wins"])

        # update game wins rate label
        self.lbl_game_win_rate["text"] = "Win Rate : " + str(round_status["win_rate"]) + " % "

        # display guess count label
        self.lbl_guess_count.place(x=10,y=120,width=125,height=35)
        self.lbl_guess_count["text"] = "Guess : 0/{0}".format(self.hm.get_max_guess())
        
        # display guessed chars label
        self.lbl_guess_chars.place(x=135,y=120,width=540,height=35)
        self.lbl_guess_chars["text"] = "Guesses : "
        
        # display button make guess
        self.btn_make_guess.place(x=282,y=180,width=120,height=30)
        

    def GButton_962_command(self):
        print("command")


    def GButton_290_command(self):
        print("command")


    def GButton_279_command(self):
        print("command")

    def display_info(self, title, message):
        msgbox.showinfo(title, message)

    def display_warning(self, title, message):
        msgbox.showwarning(title, message)

    def btn_make_guess_command(self):
                
        guess_string = inputbox.askstring(title="Guess",prompt="Enter your Guess:")
        if not isinstance(guess_string, str):
            return None
        
        guess_string = guess_string.strip() 
        if len(guess_string)==0:
            return None
        guess_char = guess_string[0]

        # invoke make_guess in hangman object
        response = self.hm.make_guess(guess_char)

        # analyse response
        success = response["success"]
        msg = response["msg"]
        guess_count = response["guess_count"]

        # update guess count and guessed chars
        self.lbl_guess_count["text"] = "Guess : {0}/{1}".format(guess_count,self.hm.get_max_guess())
        self.lbl_guess_chars["text"] = "Guesses : " + ",".join(self.hm.get_guessed_chars())

        # update hang word
        self.lbl_hang_word.configure(text=self.hm.get_hang_word())

       
        if success == 2:
            self.display_info("Correct Guess",msg)        

        if success == 0:
            self.display_warning("Wrong Guess",msg)

        if success == 1:
            self.display_info("You Win", msg)

        if self.hm.is_game_over():
            self.__restore_game_over_state()
            

    def __restore_game_over_state(self):
        # this function restore the elements state to the way it should be when the
        # game is over or there is no ongoing game
        # display all rounds so far            
        self.hm.get_game_rounds()
            
        # update win area
        round_status = self.hm.get_round_status()
        self.lbl_game_round["text"] = "Game : " + str(round_status["rounds"])
            
            
        # reposition hang word label and change its color
        self.lbl_hang_word["fg"] = "#999999"            
        self.lbl_hang_word.place(x=0,y=100,width=684,height=60)
        self.lbl_game_wins["text"] = "Wins : " + str(round_status["wins"])
        self.lbl_game_win_rate["text"] = "Win Rate : " + str(round_status["win_rate"]) + "% "
            
        # hide guess and make guess button (guess area)
        self.lbl_guess_count.place_forget()
        self.lbl_guess_chars.place_forget()
        self.btn_make_guess.place_forget()
            
        # enable Play Game button
        self.btn_start["state"] = "normal"

        # enable setting button
        self.btn_setting["state"] = "normal"

        # disable give up button again
        self.btn_give_up["state"] = "disabled"
        
    
    def btn_game_history_command(self):
        window_1 = tk.Toplevel(self.__root)
        window_1.title("Game History")
        #setting window size
        width=340
        height=291
        screenwidth = self.__root.winfo_screenwidth()
        screenheight = self.__root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        window_1.geometry(alignstr)
        window_1.resizable(width=False, height=False)        
        
        window_1.grab_set() # make other window disabled

        listBox = tk.Listbox(window_1, width=200, height=250)

        game_status = {1: "Win", 0:"Lost", 3: "Gave Up"}
        game_rounds = self.hm.get_game_rounds()
        
        for i, game_round in enumerate(game_rounds):
            listBox.insert(i, "{0}.  {1} \t |  {2} \t |  {3}".format(
                i+1,
                game_round["word"],
                ",".join(game_round["guessed_chars"]),
                game_status[game_round["status"]]
                ))
                
        listBox.pack()

        window_1.mainloop()

    def btn_setting_command(self):
        window_1 = tk.Toplevel(self.__root)
        window_1.title("Setting")
        #setting window size
        width=200
        height=100
        screenwidth = self.__root.winfo_screenwidth()
        screenheight = self.__root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        window_1.geometry(alignstr)
        window_1.resizable(width=False, height=False)    
        
        window_1.grab_set() # make other window disabled

        
        GLabel_443=tk.Label(window_1)
        GLabel_443["borderwidth"] = "2px"
        ft = tkFont.Font(family='Times',size=12)
        GLabel_443["font"] = ft
        GLabel_443["fg"] = "#333333"
        GLabel_443["justify"] = "center"
        GLabel_443["text"] = "Max Guess"
        GLabel_443["relief"] = "flat"
        GLabel_443.place(x=0,y=0,width=91,height=30)

        max_guess_text = tk.StringVar()
        GLineEdit_355=tk.Entry(window_1,textvariable = max_guess_text)
        GLineEdit_355["borderwidth"] = "2px"
        ft = tkFont.Font(family='Times',size=12)
        GLineEdit_355["font"] = ft
        GLineEdit_355["fg"] = "#333333"
        GLineEdit_355["justify"] = "center"
        GLineEdit_355.place(x=110,y=0,width=70,height=25)
        max_guess_text.set(str(self.hm.get_max_guess()))

        GLabel_962=tk.Label(window_1)
        GLabel_962["borderwidth"] = "2px"
        ft = tkFont.Font(family='Times',size=12)
        GLabel_962["font"] = ft
        GLabel_962["fg"] = "#333333"
        GLabel_962["justify"] = "center"
        GLabel_962["text"] = "Hang Char"
        GLabel_962.place(x=10,y=30,width=70,height=25)

        hang_char_text = tk.StringVar()
        GLineEdit_899=tk.Entry(window_1, textvariable = hang_char_text)
        GLineEdit_899["borderwidth"] = "2px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_899["font"] = ft
        GLineEdit_899["fg"] = "#333333"
        GLineEdit_899["justify"] = "center"
        GLineEdit_899.place(x=110,y=30,width=70,height=25)
        hang_char_text.set(self.hm.get_hang_char())

        def btn_save_setting_command():
            new_max_guess = max_guess_text.get().strip()
            new_hang_char = hang_char_text.get().strip()

            self.hm.set_max_guess(int(new_max_guess))
            self.hm.set_hang_char(new_hang_char)

            window_1.destroy()
            
        GButton_876=tk.Button(window_1)
        GButton_876["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=12)
        GButton_876["font"] = ft
        GButton_876["fg"] = "#000000"
        GButton_876["justify"] = "center"
        GButton_876["text"] = "Save"
        GButton_876.place(x=50,y=60,width=93,height=30)
        GButton_876["command"] = btn_save_setting_command
        

        window_1.mainloop()



        
