from project04 import *
from project04classes import *
import unittest
from unittest.mock import patch

class TestProject04(unittest.TestCase):

    def test_validEntryInt(self):
        '''Summary of test_validEntryInt() Test
        This test checks to make sure user input 
        '''
        firstValue = validEntry("1")
        secondValue = 2
        self.assertEqual(type(firstValue),type(secondValue))

    def test_validEntryFloat(self):
        firstValue = validEntry("2.5")
        secondValue = 3.14
        self.assertEqual(type(firstValue),type(secondValue))

    def test_validEntryFalse(self):
        self.assertFalse(validEntry("Two"))

    def test_perimeter(self):
        shape1 = Rectangle(4,4)
        firstValue = shape1.perimeter()
        secondValue = 16
        self.assertEqual(firstValue, secondValue)

    def test_area(self):
        shape1 = Rectangle(5,5)
        firstValue = shape1.area()
        secondValue = 25
        self.assertEqual(firstValue, secondValue)

    def test_volume(self):
        shape1 = Parallelepiped(4,4,4)
        firstValue = shape1.volume()
        secondValue = 64
        self.assertEqual(firstValue, secondValue)

    @patch('project04classes.display')
    def test_display(self, mock_print):
        mock_print.return_value = f'''The dimensions of the Rectangle are:
Length = 4
Width = 4
Area = 16
Perimeter = 16
'''

        
        shape1 = Rectangle(4,4)
        firstValue = shape1.display()
        secondValue = "String"
        self.assertEqual(type(shape1.display()),type(secondValue))
        
        
if __name__ == "__main__":
    unittest.main()
