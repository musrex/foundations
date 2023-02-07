import unittest
from project03 import *

board1 = [ [" S "]*grid_size for i in range(grid_size) ]

board2 = [ [" . "]*grid_size for i in range(grid_size) ]

result = isGameOver(board2)

print(result)