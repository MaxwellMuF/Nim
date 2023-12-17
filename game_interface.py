import time 
import json
from nim import train, play


class Player:
    def __init__(self, path_highscore="highscore.json", test_mode = False):
        self.test_mode = test_mode
        self.name = None
        self.difficulty = None
        self.ai_trained = None
        self.path_highscore = path_highscore
        self.highscore = self.get_highscore_data()
        self.tabs = "\t" 
        self.str_dict = {
            "call_1":
            "Welcome to the project: \"Play Nim! Try to beat the AI!\" You will learn the game Nim," +\
            "get some backgrounds and finily will mess with a reinforcement learning AI. You will train that AI with your" +\
            "hyperparameters and play agaist it.",

            "game_menu_1": 
            "Hello {}. You have three options on how to proceed: information mode (type \'info\'), " +\
            "game mode (type \'game\') or see highscore (type \'score\').\n" +\
            "Tip: You can type \'exit\' for each input and the program will end immediately.",

            "history_mode_1": 
            "You are in the information mode. Would you to learn more about: The history of Nim (type \'hist\'), " +\
            "the rules of Nim (type \'rules\'),\n" +\
            "the AI you will train on Nim (type \'info AI\'), a short introduction to RE learning (type \'info RE\'), " +\
            "or do you want to go the menu (type \'menu\')?",

            "history_mode_2": 
            self.tabs + "Variants of nim have been played since ancient times.\n" +\
            self.tabs + "The game is said to have originated in China—it closely resembles the Chinese game of 捡石子 jiǎn-shízi,\n" +\
            self.tabs + "or \"picking stones\" —but the origin is uncertain; the earliest European references to nim are from \n" +\
            self.tabs + "the beginning of the 16th century. Its current name was coined by Charles L. Bouton of Harvard University,\n" +\
            self.tabs + "who also developed the complete theory of the game in 1901, but the origins of the name were never fully explained.\n" +\
            self.tabs + "The Oxford English Dictionary derives the name from the German verb nimm, meaning \"take\".\n" +\
            self.tabs + "Read more or check the source: https://en.wikipedia.org/wiki/Nim",

            "history_mode_3": 
            self.tabs + "Nim is a mathematical game of strategy in which two players take turns removing (or \"nimming\") \n" +\
            self.tabs + "objects from distinct heaps or piles. On each turn, a player must remove at least one object, and may remove any \n" +\
            self.tabs + "number of objects provided they all come from the same heap or pile. Depending on the version being played, the \n" +\
            self.tabs + "goal of the game is either to avoid taking the last object or to take the last object. \n" +\
            self.tabs + "Read more or check the source: https://en.wikipedia.org/wiki/Nim",

            "train_ai_1": 
            "Congratulations. Now you are ready to train the AI. Here is an overview of how well you want to train them and how hard it will be for them:" +\
            "\n{:10}{:>6}".format("Easy:", "500") +\
            "\n{:10}{:>6}".format("Medium:", "1000") +\
            "\n{:10}{:>6}".format("Hard:", "5000") +\
            "\n{:10}{:>6}".format("Expert:", "10000"),

            "train_ai_2": # Update highscore with every call of self.train_ai()
            "\n{:10}{:>6}",

            "keep_or_train_1": 
            "Your AI is already trained! You trained the AI {} times! " +\
            "Do you want to keep this AI or would you like to train another one?"


        }
    
    def __call__(self):
        if self.test_mode:
            pass
        print(self.str_dict["call_1"])
        self.name = input("But first, whats your name? ")
        self.game_menu()

    def get_highscore_data(self):
        try:
            with open(self.path_highscore, "r") as json_file:
                highscore_dict = json.load(json_file)
            return highscore_dict
        except:
            self.highscore = {}
            self.save_highscore()
            return self.highscore
        
    def save_highscore(self):
        with open(self.path_highscore, "w") as json_file:
                json.dump(self.highscore, json_file)
        return

    def show_highscore(self):
        highscore_keys = sorted([int(i) for i in self.highscore.keys()], reverse=True)
        print("{:>2}.{:>6}:{:>8},{:>5}  {}".format("Nr","train", "wins AI", "Human", "Players"))
        for idx,score_key in enumerate(highscore_keys):
            list_wins = self.highscore[str(score_key)][1]
            list_score_names = ", ".join(_name for _name in self.highscore[str(score_key)][0])
            print(f"{idx+1:>2}.{score_key:>6}:{list_wins[0]:>8},{list_wins[1]:<5}  {list_score_names}")
        time.sleep(2)
        return
    
    def new_highscore(self, winner):
        # Difficulty is in highscore
        if str(self.difficulty) in self.highscore.keys():
            # If player wins and is not in winner_list
            if winner != "AI" and self.name not in self.highscore[str(self.difficulty)][0]:
                self.highscore[str(self.difficulty)][0].append(self.name)
            # If AI wins
            if winner == "AI":
                self.highscore[str(self.difficulty)][1][0] += 1
            # Else player wins
            else:
                self.highscore[str(self.difficulty)][1][1] += 1
        # Difficulty not in highscore
        else:
            # append new difficulty (train_epochs)
            self.highscore[str(self.difficulty)] = [[], [0,0]]
            # if player wins
            print(winner)
            if winner != "AI":
                self.highscore[str(self.difficulty)][0].append(self.name)
                self.highscore[str(self.difficulty)][1][1] += 1
            #if AI wins
            else:
                self.highscore[str(self.difficulty)][1][0] += 1
        return

    def get_highscore_1st_place(self):
        highscore_keys = sorted([int(i) for i in self.highscore.keys()], reverse=True)
        # Iterate highscore_keys (sorted)
        for score_key in highscore_keys:
            # Check if there is a human winner
            if self.highscore[str(score_key)][0]:
                return score_key
        else:
            return 0


    def game_menu(self):
        print()
        print(self.str_dict["game_menu_1"].format(self.name))
        input_game_menu = input("Type what you want to do: ")
        if input_game_menu == "info":
            self.history_mode()
        elif input_game_menu == "game":
            self.keep_or_train()
        elif input_game_menu == "score":
            self.show_highscore()
            self.game_menu()
        elif input_game_menu == "exit":
            self.save_highscore()
            pass
        else:
            print()
            print("I'm afraid I didn't understand your request. Lets try it again")
            self.game_menu()
        return

    def history_mode(self):
        print()
        print(self.str_dict["history_mode_1"])
        input_history_mode = input("Type what you want to read: ")
        if input_history_mode == "hist":
            print()
            print(self.str_dict["history_mode_2"])
            self.history_mode()
        elif input_history_mode == "rules":
            print()
            print(self.str_dict["history_mode_3"])
            self.history_mode()
        elif input_history_mode == "menu":
            self.game_menu()
        elif input_history_mode == "exit":
            self.save_highscore()
            pass
        else:
            print()
            print("I'm afraid I didn't understand your request. Lets try it again")
            self.history_mode()
        return

    def train_ai(self):
        print()
        print(self.str_dict["train_ai_1"] + self.str_dict["train_ai_2"].format("Highscore", self.get_highscore_1st_place()))
        input_train_ai = input("How many steps of training do you want? ")
        try:
            self.difficulty = int(input_train_ai)
            print(f"Ok, lets train the AI {self.difficulty} times!")
            self.ai_trained = train(self.difficulty)
            print()
            print("The training is complete. The AI is ready! Are you ready to play?")
            self.play_game()
        except:
            if input_train_ai == "menu":
                self.game_menu()
            elif input_train_ai == "exit":
                self.save_highscore()
                pass
            else:
                print()
                print("I'm afraid I didn't understand your request. Lets try it again.")
                self.train_ai()
        return

    def keep_or_train(self):
        if self.ai_trained:
            print()
            print(self.str_dict["keep_or_train_1"].format(self.difficulty))
            input_keep_or_train = input("Type \'keep\' to keep your AI or \'train\' to train a new one. ")
            if input_keep_or_train == "keep":
                self.play_game()
            elif input_keep_or_train == "train":
                self.train_ai()
            elif input_keep_or_train == "menu":
                self.game_menu()
            elif input_keep_or_train == "exit":
                self.save_highscore()
                pass
            else:
                print()
                print("I'm afraid I didn't understand your request. Lets try it again")
                self.keep_or_train()
        else:
            self.train_ai()
        return

    def play_game(self):
        print()
        input_play_game = input("Type \'play\' to play, \'score\' to show highscore or \'menu\' to go to the menu! ")
        if input_play_game == "play":
            winner = play(self.ai_trained, self.name)
            self.new_highscore(winner)
            print()
            time.sleep(2)
            print("Whats next? Do you want to play again?")
            self.play_game()
        elif input_play_game == "score":
            self.show_highscore()
            self.play_game()
        elif input_play_game == "menu":
            self.game_menu()
        elif input_play_game == "exit":
            self.save_highscore()
            pass
        else:
            print()
            print("I'm afraid I didn't understand your request. Lets try it again")
            self.play_game()
        return