import pygame
import numpy as np
from math import inf


pygame.init()
WINDOW = pygame.display.set_mode((600,600))
pygame.display.set_caption("Tic-Tac-Toe")

Board = np.array([[0,0,0],[0,0,0],[0,0,0]]) #Zero is empty, One is X, Two is O
#The player is representing X

def checkWinner(board):
    # Check rows for win
	for row in board:
		if row[0] == row[1] == row[2] and row[0] != 0:
			if row[0] == 1:
				return 1
			else:
				return 2

    # Check columns for win
	for col in range(3):
		if board[0][col] == board[1][col] == board[2][col] and board[0][col] != 0:
			if board[0][col]==1:
				return 1
			else:
				return 2

    # Check diagonals for win
	if board[0][0] == board[1][1] == board[2][2] and board[0][0] != 0:
		if board[0][0]==1:
			return 1
		else:
			return 2
	if board[0][2] == board[1][1] == board[2][0] and board[0][2] != 0:
		if board[0][2]==1:
			return 1
		else:
			return 2
	
	if isFull(board):
		return 0
	return -1


def drawWinnerDisplay():
	if checkWinner(Board) == 1:
		resultText="Winner"
		font = pygame.font.SysFont("Arial", 72)
		text = font.render(resultText, True, (255,255,255), (0,0,0))
		textRect = text.get_rect()
		textRect.center = (300, 300)
		WINDOW.fill((24,24,24))
		drawGameOutlines()
		WINDOW.blit(text, textRect)
		pygame.display.update()
	if checkWinner(Board) == 2:
		resultText="Loser"
		font = pygame.font.SysFont("Arial", 72)
		text = font.render(resultText, True, (255,255,255), (24,24,24))
		textRect = text.get_rect()
		textRect.center = (300, 300)
		WINDOW.fill((24,24,24))
		drawGameOutlines()
		WINDOW.blit(text, textRect)
		pygame.display.update()
	if checkWinner(Board) == 0:
		resultText="Tie"
		font = pygame.font.SysFont("Arial", 72)
		text = font.render(resultText, True, (255,255,255), (24,24,24))
		textRect = text.get_rect()
		textRect.center = (300, 300)
		WINDOW.fill((24,24,24))
		drawGameOutlines()
		WINDOW.blit(text, textRect)
		pygame.display.update()

def markBoard(array):
    for i in range(3):
        for j in range(3):
            match array[i][j]:
                case 1:
                    pygame.draw.line(WINDOW,(0,255,0),(i*200+25,j*200+25),(i*200+175,j*200+175),width=5)
                    pygame.draw.line(WINDOW,(0,255,0),(i*200+175,j*200+25),(i*200+25,j*200+175),width=5)
                case 2:
                    pygame.draw.circle(WINDOW,(255,0,0),(i*200+100,j*200+100),80,width=3)
    pygame.display.update()



def drawGameOutlines():
    WINDOW.fill((24,24,24))
    pygame.draw.line(WINDOW,(255,255,255),(0,200),(600,200),width=3)
    pygame.draw.line(WINDOW,(255,255,255),(0,400),(600,400),width=3)
    pygame.draw.line(WINDOW,(255,255,255),(200,0),(200,600),width=3)
    pygame.draw.line(WINDOW,(255,255,255),(400,0),(400,600),width=3)
    pygame.display.update()

def getUserInput():
    if 0<=pygame.mouse.get_pos()[0]<=200 and 0<=pygame.mouse.get_pos()[1]<=200:
        if Board[0][0] == 0:
            Board[0][0]=1
    elif 200<=pygame.mouse.get_pos()[0]<=400 and 0<=pygame.mouse.get_pos()[1]<=200:
        if Board[1][0] == 0:
            Board[1][0]=1
    elif 400<=pygame.mouse.get_pos()[0]<=600 and 0<=pygame.mouse.get_pos()[1]<=200:
        if Board[2][0] == 0:
            Board[2][0]=1
    elif 0<=pygame.mouse.get_pos()[0]<=200 and 200<=pygame.mouse.get_pos()[1]<=400:
        if Board[0][1] == 0:
            Board[0][1]=1
    elif 200<=pygame.mouse.get_pos()[0]<=400 and 200<=pygame.mouse.get_pos()[1]<=400:
        if Board[1][1] == 0:
            Board[1][1]=1
    elif 400<=pygame.mouse.get_pos()[0]<=600 and 200<=pygame.mouse.get_pos()[1]<=400:
        if Board[2][1] == 0:
            Board[2][1]=1
    elif 0<=pygame.mouse.get_pos()[0]<=200 and 400<=pygame.mouse.get_pos()[1]<=600:
        if Board[0][2] == 0:
            Board[0][2]=1
    elif 200<=pygame.mouse.get_pos()[0]<=400 and 400<=pygame.mouse.get_pos()[1]<=600:
        if Board[1][2] == 0:
            Board[1][2]=1
    elif 400<=pygame.mouse.get_pos()[0]<=600 and 400<=pygame.mouse.get_pos()[1]<=600:
        if Board[2][2] == 0:
            Board[2][2]=1

# Python3 program to find the next optimal move for a player
player, opponent = 2 , 1


# This function returns true if there are moves
# remaining on the board. It returns false if
# there are no moves left to play.
def isMovesLeft(board) :

	for i in range(3) :
		for j in range(3) :
			if (board[i][j] == 0) :
				return True
	return False

def isFull(board) :

	for i in range(3) :
		for j in range(3) :
			if (board[i][j] == 0) :
				return False
	return True

# This is the evaluation function as discussed
# in the previous article ( http://goo.gl/sJgv68 )
def evaluate(b) :

	# Checking for Rows for X or O victory.
	for row in range(3) :	
		if (b[row][0] == b[row][1] and b[row][1] == b[row][2]) :	
			if (b[row][0] == player) :
				return 10
			elif (b[row][0] == opponent) :
				return -10

	# Checking for Columns for X or O victory.
	for col in range(3) :
	
		if (b[0][col] == b[1][col] and b[1][col] == b[2][col]) :
		
			if (b[0][col] == player) :
				return 10
			elif (b[0][col] == opponent) :
				return -10

	# Checking for Diagonals for X or O victory.
	if (b[0][0] == b[1][1] and b[1][1] == b[2][2]) :
	
		if (b[0][0] == player) :
			return 10
		elif (b[0][0] == opponent) :
			return -10

	if (b[0][2] == b[1][1] and b[1][1] == b[2][0]) :
	
		if (b[0][2] == player) :
			return 10
		elif (b[0][2] == opponent) :
			return -10

	# Else if none of them have won then return 0
	return 0

# This is the minimax function. It considers all
# the possible ways the game can go and returns
# the value of the board
def minimax(board, depth, isMax) :
	score = evaluate(board)

	# If Maximizer has won the game return his/her
	# evaluated score
	if (score == 10) :
		return score

	# If Minimizer has won the game return his/her
	# evaluated score
	if (score == -10) :
		return score

	# If there are no more moves and no winner then
	# it is a tie
	if (isMovesLeft(board) == False) :
		return 0

	# If this maximizer's move
	if (isMax) :	
		best = -1000

		# Traverse all cells
		for i in range(3) :		
			for j in range(3) :
			
				# Check if cell is empty
				if (board[i][j]==0) :
				
					# Make the move
					board[i][j] = player

					# Call minimax recursively and choose
					# the maximum value
					best = max( best, minimax(board,
											depth + 1,
											not isMax) )

					# Undo the move
					board[i][j] = 0
		return best

	# If this minimizer's move
	else :
		best = 1000

		# Traverse all cells
		for i in range(3) :		
			for j in range(3) :
			
				# Check if cell is empty
				if (board[i][j] == 0) :
				
					# Make the move
					board[i][j] = opponent

					# Call minimax recursively and choose
					# the minimum value
					best = min(best, minimax(board, depth + 1, not isMax))

					# Undo the move
					board[i][j] = 0
		return best

# This will return the best possible move for the player
def findBestMove(board) :
	bestVal = -1000
	bestMove = (-1, -1)

	# Traverse all cells, evaluate minimax function for
	# all empty cells. And return the cell with optimal
	# value.
	for i in range(3) :	
		for j in range(3) :
		
			# Check if cell is empty
			if (board[i][j] == 0) :
			
				# Make the move
				board[i][j] = player

				# compute evaluation function for this
				# move.
				moveVal = minimax(board, 0, False)

				# Undo the move
				board[i][j] = 0

				# If the value of the current move is
				# more than the best value, then update
				# best/
				if (moveVal > bestVal) :			
					bestMove = (i, j)
					bestVal = moveVal
    
	return bestMove


def main():
	run=True
	drawGameOutlines()
	clock = pygame.time.Clock()
	while run:
		clock.tick(15)
		#drawWinnerDisplay()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run=False
			if event.type == pygame.MOUSEBUTTONUP:
				if isMovesLeft(Board):
					getUserInput()
					drawGameOutlines()
					bestmove=findBestMove(Board)
					if Board[bestmove[0]][bestmove[1]]!=1:
						Board[bestmove[0]][bestmove[1]]=2
					markBoard(Board)
				if checkWinner(Board)>=0:
					drawWinnerDisplay()
					Board[Board>0]=0
	pygame.quit()

if __name__ == "__main__":
    main()