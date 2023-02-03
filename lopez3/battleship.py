import random

# the size of the 2 d array
grid_size = 10
# this is the array declaration
grid = [ ['']*grid_size for i in range(grid_size) ]
# we use this list to verify that ships aren't being placed in the same location
ships = []
num_of_ships = 5

# display the grid (2d array)
def drawBoard(myBoard):
    i = j = 0
    # this print statement, repeated throughout this function, creates our horizontal borders
    print('''
 ____ _____ _____ _____ __    _____ _____ _____ _____ _____ 
| _  |  _  |_   _|_   _|  |  |   __|  |  |     |  _  |   __|
| _ -|     | | |   | | |  |__|__   |     |-   -|   __|__   |
|____|__|__| |_|   |_| |_____|_____|__|__|_____|__|  |_____|                                                          
 ''')
    print("+---+---+---+---+---+---+---+---+---+---+---+")
    # this print statement gives us the top row, horizontal coordinates
    print("| * "," 0 "," 1 "," 2 "," 3 "," 4 "," 5 "," 6 "," 7 "," 8 "," 9 |", sep="|")
    for i in range(grid_size):
        print("+---+---+---+---+---+---+---+---+---+---+---+")
        # this print statement gives 
        print("| " + str(i) , end=" |")
        for j in range(grid_size):
            print("" + myBoard[i][j] , end = "|")
        print()
    print("+---+---+---+---+---+---+---+---+---+---+---+")
    return(myBoard)
        


# initilize the 2 d array (the grid)
def setupBoard(grid):
    global ships
    i = j = 0
    while i < grid_size:
        while j < grid_size:
            # store the string "i, j" into the array
            grid[i][j] = " . " 
            j += 1
        j = 0
        i += 1

    x = 0

    while x < num_of_ships: 
        randomRow = random.randint(0, grid_size - 1)
        randomCol = random.randint(0, grid_size - 1)    
        if grid[randomRow][randomCol] not in ships:
            ships.append(grid[randomRow][randomCol])
        if grid[randomRow][randomCol] in ships:
            grid[randomRow][randomCol] = " S "
            x += 1
            
    return(grid)


def hitOrMiss(myBoard, row, col):
    # implement the hit or miss functionality here    
    row = int(row)
    col = int(col)
    if grid[row][col] == " S ":
        grid[row][col] = " X "
        return True
    else:
        grid[row][col] == " O "
        return False


def isGameOver(myBoard):
    # check if there are ships remaining on the grid.
    # if there are ships remaining, return false else return true
    return False


# the main function!
def main(myBoard):
    
    # first set up the array
    setupBoard(myBoard)
    # now display the array
    run = True

    while run:
        drawBoard(myBoard)
        print()
        print("Captain, please enter your coordinates: ")
        row = input("X Coordinates: ")
        col = input("Y Coordinates: ")
        hitOrMiss(myBoard, row, col)


# don't forget to call the main function
# lastly do NOT forget to pass the array we declared
main(grid)


