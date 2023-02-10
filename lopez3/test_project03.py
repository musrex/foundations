import unittest
from project03 import *

# this board is entirely ships, so for testing every shot should hit
# and the game is not over 
board1 = [ [" S "]*grid_size for i in range(grid_size) ]

#this board is entirely empty, so for testing every shot should miss
# and the game should be over
board2 = [ [" . "]*grid_size for i in range(grid_size) ]
# we use this list to verify that ships aren't being placed in the same location


class TestProject03(unittest.TestCase): 
    
    def test_isGameOverFalse(self):
        '''Summary of test_isGameOverFalse
        This test asserts a condition in which ISGAMEOVER() returns FALSE

        Parameters
        isGameOver(function): This function checks whether there are
        ships remaining on the board.
        
        board1(array):  board1 is a entirely full of ships, and should return
        FALSE, meaning the game is not over.
        '''
        self.assertFalse(isGameOver(board1))

    def test_isGameOverTrue(self):
        '''Summary of test_isGameOverTrue
        This test asserts a condition in which ISGAMEOVER() returns TRUE

        Parameters
        isGameOver(function): This function checks whether there are
        ships remaining on the board.
        
        board2(array):  board2 is a empty of any ships, and should return
        TRUE, meaning the game is over.
        '''
        self.assertTrue(isGameOver(board2))

    def test_checkHit(self):
        '''Summary of test_checkHit
        This test asserts a condition in which HITORMISS() returns TRUE

        Parameters
        hitOrMiss(function): This function checks whether the coordinates
        input by the user match the coordinates of a ship
        
        arg1, board1(array):  board1 is a entirely full of ships, and should
        return TRUE, meaning the a ship was hit.

        arg2,arg3, (int): these args are positions on the board. Make sure you
        pass ints that are in the range of your board.

        firstValue(boolean): Stores the value of HITORMISS to be compared
        to secondValue

        secondValue(boolean): The controlled value we pass through that the
        HITORMISS function needs to match with.
        '''
        firstValue = hitOrMiss(board1, 1, 1)
        secondValue = True
        message = "Hit"
        self.assertEqual(firstValue, secondValue, message)

    def test_checkMiss(self):
        '''Summary of test_checkMISS
        This test asserts a condition in which HITORMISS() returns FALSE

        Parameters
        hitOrMiss(function): This function checks whether the coordinates
        input by the user match the coordinates of a ship
        
        arg1, board2(array):  board2 is empty of ships, and should
        return FALSE, meaning no ship was hit.

        arg2,arg3, (int): these args are positions on the board. Make sure you
        pass ints that are in the range of your board.

        firstValue(boolean): Stores the value of HITORMISS to be compared
        to secondValue

        secondValue(boolean): The controlled value we pass through that the
        HITORMISS function needs to match with.
        '''
        firstValue = hitOrMiss(board2, 1, 1)
        secondValue = False
        message = "Miss"
        self.assertEqual(firstValue, secondValue)
    
    def test_setupBoardSpaces(self):
        self.assertEqual(len(water) - len(ships), 95)

    def test_setupBoardShips(self):
        setupBoard()
        self.assertEqual(len(ships), num_of_ships)

if __name__ == "__main__":
    unittest.main()
