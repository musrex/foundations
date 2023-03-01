from project06 import *
from options import *
from transports import *
import unittest

class TestProject06(unittest.TestCase):
    
    def testOptions1(self):
    '''Summary of TESTOPTIONS1 test:
    This test checks to see if the OPTIONS function
    returns 
    '''
        firstValue = options("1")
        secondValue = 1
        self.assertEqual(firstValue,secondValue)

    def testOptions4(self):
        firstValue = options("4")
        secondValue = 4
        self.assertEqual(firstValue,secondValue)
    
    def testEast(self):
        terminal = Terminal()
        terminal.west(1)
        terminal.east(2)        
        result = terminal.items
        self.assertEqual(result[1], 2)

    def testWest(self):
        terminal = Terminal()
        terminal.east(1)
        terminal.east(2)
        terminal.west(3)
        result = terminal.items
        self.assertEqual(result[0], 3)

    def testAddTransport1(self):
        direction = 1
        terminal = Terminal()
        transport = 3
        result = addTransport(direction,terminal,transport)
        self.assertTrue(result)

    def testAddTransport2(self):
        direction = 4
        terminal = Terminal()
        transport = 3
        result = addTransport(direction,terminal,transport)
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()