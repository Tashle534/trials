from  single_player_tictactoe import single_player 

def user_choice():
    
    exit_game = False
    while exit_game:
        user_resp = input("1 - single player \n 2 - dual player ")
        if user_resp == "1":
            single_player()
            exit_game = True
        elif user_resp =="2":
            dual_player()
            exit_game = True
        else:
            print("invalid option, please select one of the given options")
            exit_game = True

