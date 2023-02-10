# Assignment 3 Write Up
This is a Battleship style game. A board will be printed out to the users screen, and then they'll be prompted to enter coordinates. Upon sinking all enemy ships, the user will win and the game will be over.

# Assignment 3 Algorithm
1. First we create a 10 x 10 grid.
2. Next, we use that grid to create our game board, with empty spaces, ships, and the headers for our columns and rows.
3. We iterate through the grid, appropriately placing items on it. Ships placed should be tracked, so we know what our target goal is. We should also track empty spaces for testing.
4. Then we take in input from the user, and use that input to find the corresponding place in the grid. This process should loop until the appropriate input is entered.
5. We take that input and pass it through a function that checks to see whether the user hit a ship, or missed. Our function should also track the number of ships hit.
6. Next, we take the number of ships hit from the previous function, and compare that to the ships placed from step 3 to determine whether there are any targets left.
7. We loop through this process, steps 4 - 6, redrawing the board for every turn and updating it based on hits and misses.
8. After all targets have been eliminated, we should get a game over that ends the loop.
