def single_player():
    
    from random import randint
    
    
    grid = [ [0,1,2] ,[3,4,5] , [6,7,8] ]
    exit_game = True
    exit_player_move= False
    user_player = input("Please pick your player : X / O ").strip().upper()
    computer_move = randint(0,8)
    
    if user_player not in("X","O"):
        print("invalid option")
        return
    
    print(f"You've selected {user_player}, Let us begin ! ! ☺️ ")
    
    def printing_grid() :
        for grid_row in grid:
            print(grid_row)
    
    printing_grid()
    
    print("Pick your box, using the numbers as reference")
    
    while  exit_game:
        
        def user_move():
            while exit_player_move: 
                #
                try:
                    move = int(input(f"Please enter {user_player} move, \n a number between 0 - 8 "))
                    
                    if move > 8 and move < 0:  #checking if the move number is within range
                        continue
                    
                    
                    row,col = divmod(move,3) #divmod function returns the answer and the remainder
                                                        #checking if the box is full already 
                    if grid[row][col] != " " :
                        grid[row][col] = user_player
                        
                        for grid_row in grid:
                            print(grid_row)
                            
                        exit_player_move = True
                        
                    else:
                        print("space full, please pick another one ")
                        
                except ValueError:
                        print("invalid range, please pick between 0 - 8 ")
                        
                #making the computer's moves
                
                
                

single_player()