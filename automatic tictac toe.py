import numpy as np 
import random
from time import sleep

def create_board(): #creating the bord to play
    return np.zeros((3,3) ,dtype=int)
    
def possiblities(board): #possibilities on the play board
    return [(i,j) for i in range(2) for j in range(3) if(board[i][j]==0)]

def random_place(board,player): #random choices by the players
    game=random.choice(possiblities(board))
    board[game]=player
    return board
    
def win_row(board,player): #determing winned row
    return any(all(cell==player for cell in row) for row in board)
    
def win_column(board,player):  #determing winned column
    return any(all (row[i]==player for row in board) for i in range(3))
    
def diagonal_win(board,player):  #determing winned diagonal
    return all(board[i][i]==player for i in range(3)) or all(board[i][2-i]==player for i in range(3))

def evaluate_board(board):  #evaluating the board
    for player in [1,2]:
        if(win_row(board,player) or win_column(board,player) or diagonal_win(board,player)):
            return player
    return "DRAW" if np.all (board !=0 ) else 0
    
def play_game(): #play the game
    board, winner, move = create_board(), 0, 1
    print(board)
    sleep(1)

    while winner == 0:
        for player in [1, 2]:
            board = random_place(board, player)
            print(f"\nBoard after move {move}:\n{board}")
            sleep(1)
            move += 1
            winner = evaluate_board(board)
            if winner != 0:
                break

    return winner

# Run the game
print(f"\nWinner is: {play_game()}")