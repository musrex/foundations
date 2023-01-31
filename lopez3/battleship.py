import random

grid_size = 10
num_of_ships = 5
myBoard = [['']*grid_size for i in range(grid_size)]

def drawBoard(myBoard):
	# here I draw my board

    for i in range(grid_size):
        for j in range(grid_size):
            print(myBoard[i][j], end = "")
        return
	
	

def setupBoard(myBoard):
    i = j = 0

    while i < grid_size:
        while j < grid_size:
            myBoard[i][j] = str(i) + "," + str(j) + ""
            j += 1
        j = 0
        j += 1

def main(myBoard):

    setupBoard(myBoard)

    drawBoad(myBoard)

main(myBoard)
