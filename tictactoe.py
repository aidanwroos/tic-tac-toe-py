#import os

#global game board
board = {7 : " ", 8 : " ", 9 : " ",
         4 : " ", 5 : " ", 6 : " ",
         1 : " ", 2 : " ", 3 : " "}
         
#print board function
def print_board():
    print("7|8|9      " + board[7] + "|" + board[8] + "|" + board[9])
    print("-+-+-      -+-+-")
    print("4|5|6  =>  " + board[4] + "|" + board[5] + "|" + board[6])
    print("-+-+-      -+-+-")
    print("1|2|3      " + board[1] + "|" + board[2] + "|" + board[3])


#set board pos values function
def set_board(pos, val):
    board[pos] = val;
    

#check win
def check_winner():
    #8 win combinations
    combinations = ["123", "456", "789", 
                    "147", "258", "369", 
                    "159", "357"]
                    
    win_comb_index = 0;
    player = ""
    
    for i in range(0,8):
        pos1 = int(combinations[i][0])
        pos2 = int(combinations[i][1])
        pos3 = int(combinations[i][2])
        
        if board[pos1].strip() and board[pos2].strip() and board[pos3].strip():
            if(board[pos1] == board[pos2] and board[pos1] == board[pos3]):
                win_comb_index = i
                player = board[pos1]
                break
        else:
            player = ""
            
    return player
    
        
def switch_turn(current_turn):
    player = (current_turn + 1) % 2
    if player == 1:
        return "X"
    elif player == 0:
        return "O"
        
        
def update_board(player, pos):
    board[pos] = player

def pos_valid(pos):
    if not board[pos].strip():
        return True
    else:
        return False
        

#main game loop
def game():
    current_turn = 0
    print("TicTacToe\n")
    
    while True:
        print_board()
        
        #receive player input
        player = switch_turn(current_turn)
        pos = int(input("Player " + player + " choose: "))
        
        if not pos_valid(pos):
            print("Spot already taken!\n")
            continue
            
        else:
            #update the board
            update_board(player, pos)
            
            #check for a win
            win = check_winner() 
            if not win:
                current_turn += 1
                print("\n")
                continue
            else:
                print("\n")
                print_board()
                print("Player " + win + " WINS!!\n")
                break
            

        #refresh screen
        #os.system('cls')
        
game()
