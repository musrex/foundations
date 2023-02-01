'''
GK 6/1/22 - A program to set up and display a 2 d array of strings
'''
import random

# the size of the 2 d array
grid_size = 10
# this is the array declaration
grid = [ ['']*grid_size for i in range(grid_size) ]

num_of_ships = 5

# display the grid (2d array)
def drawBoard(myBoard):
    i = j = 0
    print("+-+-+-+-+-+-+-+-+-+-+-+")
    print("|*","0","1","2","3","4","5","6","7","8","9|", sep="|")
    for i in range(grid_size):
        print("+-+-+-+-+-+-+-+-+-+-+-+")
        print("|" + str(i) , end="|")
        for j in range(grid_size):
            print("" + myBoard[i][j] , end = "|")
            #for x in grid:
                #print("-", end="")
        print()
    print("+-+-+-+-+-+-+-+-+-+-+-+")
        


# initilize the 2 d array (the grid)
def setupBoard(grid):
    i = j = 0
    while i < grid_size:
        while j < grid_size:
            # store the string "i, j" into the array
            grid[i][j] = "." 
            j += 1
        j = 0
        i += 1
    x = 0
    while x < num_of_ships:
        randomRow = random.randint(0, grid_size - 1)
        randomCol = random.randint(0, grid_size - 1)   
        grid[randomCol][randomRow] = "S"
        x += 1
    return(grid)

# the main function!
def main(myBoard):
    # first set up the array
    setupBoard(myBoard)

    # now display the array
    drawBoard(myBoard)

# don't forget to call the main function
# lastly do NOT forget to pass the array we declared
main(grid)


