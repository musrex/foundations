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


    def test_isGameOverTrue(self):
        self.assertFalse(isGameOver(board1))

    def test_isGameOverFalse(self):
        self.assertFalse(isGameOver(board2))

    def test_checkHit(self):
        firstValue = hitOrMiss(board1, 1, 1)
        secondValue = True
        message = "Hit"
        self.assertEqual(firstValue, secondValue, message)

    def test_checkMiss(self):
        firstValue = hitOrMiss(board2, 1, 1)
        secondValue = False
        message = "Miss"
        self.assertEqual(firstValue, secondValue)

    def test_setupBoardShips(self):
        setupBoard()
        self.assertEqual(len(ships), num_of_ships)

    def test_setupBoardSpaces(self):
        setupBoard()
        a = len(water)
        b = len(ships)
        self.assertEquals(a - b, 95)