import unittest
from project03 import isGameOver

num_ships = 0
grid = [["S"]*10 for i in range(10)]

class TestProject03(unittest.TestCase):

    def test_isGameOverTrue(self):
        num_ships = 0
        self.assertTrue(isGameOver(num_ships))
