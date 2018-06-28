##clear output use print('\n'*100)
import random
import os


def display_board(board):
	##       |       |      	empty1
	##       |       |      	Piece1
	##_______|_______|______	empty2
	##       |       |      
	##       |       |      	Piece2
	##_______|_______|______
	##       |       |      
	##       |       |       	Piece3
	##       |       |      
	empty1 = '       |       |       '
	piece1 = '   '+ board[7]+'   |   '+board[8]+'   |   '+board[9]+'   '
	empty2 = '_______|_______|_______'
	piece2 = '   '+ board[4]+'   |   '+board[5]+'   |   '+board[6]+'   '
	piece3 = '   '+ board[1]+'   |   '+board[2]+'   |   '+board[3]+'   '

	print(empty1)
	print(piece1)
	print(empty2)
	print(empty1)
	print(piece2)
	print(empty2)
	print(empty1)
	print(piece3)
	print(empty1)

def player_input():
    ## Take in input from the player
    ## everything except X or O will print "Please pick 'X' or 'O'"
    ## Capitlize function to intake small case x and o
    marker = ''
    while not(marker == 'X' or marker == 'O'):
        marker = input('Player1: Do you want to be X or O?').upper()
    
    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')
        

def place_marker(board, marker, position):
    ## Takes in board, marker, and position to replace it
    board[position] = marker


## takes in a board and a mark X or O and then checks to see that mark has won
def win_check(board, mark):
	## Win conditions, Horzontally, Vertically, and diagonally
	## 123|456|789|147|258|369|159|753
	## 8 win condtions in total
	return((board[1] == mark and board[2] == mark and board[3] == mark) or 	#123
	(board[4] == mark and board[5] == mark and board[6] == mark) or 		#456
	(board[7] == mark and board[8] == mark and board[9] == mark) or 		#789
	(board[1] == mark and board[4] == mark and board[7] == mark) or 		#147
	(board[2] == mark and board[5] == mark and board[8] == mark) or 		#258
	(board[3] == mark and board[6] == mark and board[9] == mark) or 		#369	
	(board[1] == mark and board[5] == mark and board[9] == mark) or 		#159
	(board[7] == mark and board[5] == mark and board[3] == mark))			#753


## Used to see which player goes first
def choose_first():
    r = random.randint(0,1)
    if r == 0:
        return 'Player 2'
    else:
        return 'Player 1'

## Check if space is available 
def space_check(board, position):
    return board[position] == ' '

## Check if board is full
def full_board_check(board):
    
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
        
    return position

## Ask if players want to play again
def replay():
    replay=''
    while replay == '':
        replay = input('Would you like to replay? Yes or No')
        replay.capitalize()
        if replay != 'Yes' and replay != 'No':
            print("Please enter 'Yes' or 'No'")
            replay =''
    return replay == 'Yes'

 
print('Welcome to Tic Tac Toe!') 
while True:
    # Set the game up here
    board = [' '] *10
    player1, player2 = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    
    play_game = input('Are you ready to play? Enter Yes or No.')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False
        
    while game_on:
        #Player 1 Turn
        if turn == 'Player 1':
            display_board(board)
            m = player_choice(board)
            place_marker(board, player1, m)
            if win_check(board,player1):
                print('Player 1 wins!')
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print('This was a tie!')
                    break
                else:
                    turn = 'Player 2'
            
        # Player2's turn.
        else:
            display_board(board)
            m = player_choice(board)
            place_marker(board, player2, m)
            if win_check(board,player2):
                print('Player 2 wins!')
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print('This was a tie!')
                    break
                else:
                    turn = 'Player 1'
        
    if not replay():
        break

delay = input("Press enter to finish")