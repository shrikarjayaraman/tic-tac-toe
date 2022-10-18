#TIC TAC TOE
import random
board=["-","-","-",
       "-","-","-",
       "-","-","-" ] 


curr_play="X"

Winner=None
game_run=True

#printing board
def print_board(board):
        print(board[0] + " | " + board[1] + " | " + board[2])
        print("----------")
        print(board[3] + " | " + board[4] + " | " + board[5])
        print("----------")
        print(board[6] + " | " + board[7] + " | " + board[8])

print_board(board)

def player_input(board):
    print("Your turn "+curr_play+"!")
    inp=int(input("Enter a number from 1 to 9 (Position on Board): "))
    if inp>=1 and inp<=9 and board[inp-1]=="-":
        board[inp-1]=curr_play
    else:
        print("Invalid input")


def check_hor(board):
    global Winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        Winner=board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        Winner=board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        Winner=board[6]
        return True

def check_vert(board):
    global Winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        Winner=board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        Winner=board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        Winner=board[2]
        return True

def check_diag(board):
    global Winner
    if board[0] == board[4] == board[8] and board[0] !="-":
        Winner=board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] !="-":
        Winner=board[2]
        return True   

def check_win():
    global game_run
    if check_hor(board) or check_vert(board) or check_diag(board):
        print("The winner is: "+ curr_play)
        game_run=False
        return True

def checkTie(board):
    global game_run
    if "-" not in board:
        print_board(board)
        print("It's a Tie")
        game_run=False
        return True


def switch_p():
    global curr_play
    if curr_play=="X":
        curr_play="O"
    else:
        curr_play="X"

def computer(board):
    while curr_play=="O":
        print("O's Turn: ")
        position= random.randint(0,8)
        if board[position]=="-":
            board[position]="O"
            switch_p()

while(game_run):
     player_input(board)
     print_board(board)
     if check_win():
        break
     if checkTie(board):
        break
     switch_p()
     computer(board)
     print_board(board)
     if check_win():
        break
     if checkTie(board):
        break

     