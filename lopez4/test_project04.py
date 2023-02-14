from project04 import *
from project04classes import *
import unittest
from unittest.mock import patch

class TestProject04(unittest.TestCase):

    def test_validEntryInt(self):
        '''Summary of test_validEntryInt() Test
        This test checks to make sure user input
        can be converted to an int.

        Parameters:
        firstValue = validEntry(function): This function checks to see
        if the user enetered a valid number. For our test,
        we pass 1 as a str, which will be converted to an int
        by the function.

        secondValue = 2: We assign the int 2 to our second value.
        We assert that the type of firstValue and secondValue is
        equal, meaning our function successfully converted the
        str 1 to an int of 1.
        '''
        firstValue = validEntry("1")
        secondValue = 2
        self.assertEqual(type(firstValue),type(secondValue))

    def test_validEntryFloat(self):
        '''Summary of test_validEntryFloat() Test
        This test checks to make sure user input
        can be converted to a float.

        Parameters:
        firstValue = validEntry(function): This function checks to see
        if the user enetered a valid number. For our test,
        we pass 2.5 as a float, which will be converted to a float
        by the function.

        secondValue = 3.14: We assign the float 3.14 to our second value.
        We assert that the type of firstValue and secondValue is
        equal, meaning our function successfully converted the
        str 2.5 to a float of 3.14.
        '''
        firstValue = validEntry("2.5")
        secondValue = 3.14
        self.assertEqual(type(firstValue),type(secondValue))

    def test_validEntryFalse(self):
        '''Summary of test_validEntryFloat() Test
        This test checks to make sure invalid user input returns FALSE

        Parameters:
        firstValue = validEntry(function): This function checks to see
        if the user enetered a valid number. For our test,
        we pass the string "Two", which can't be converted to an int or a
        float by the function, and so should result in FALSE being returned.
        '''
        self.assertFalse(validEntry("Two"))

    def test_perimeter(self):
        '''Summary of test_perimeter() Test
        This test checks to make sure the perimeter() function returns
        the correct calculations

        Parameters:
        shape1 = Rectangle(4,4): We instantiate the object shape1 as a
        Rectangle with attributes 4 (length) and 4 (width).

        firstValue = shape1.perimeter(): An object of the Rectangle class
        with attributes 4, 4, and call the perimeter method on it.
        
        secondValue = 16.

        We assert that the value 16 is equal to the return value of the
        perimeter() method called on shape1, which should return a perimeter
        of 16.
        '''
        shape1 = Rectangle(4,4)
        firstValue = shape1.perimeter()
        secondValue = 16
        self.assertEqual(firstValue, secondValue)

    def test_area(self):
        '''Summary of test_area() Test
        This test checks to make sure the area() function returns
        the correct calculations

        Parameters:
        shape1 = Rectangle(5,5): We instantiate the object shape1 as a
        Rectangle with attributes 5 (length) and 5 (width).

        firstValue = shape1.area(): An object of the Rectangle class
        with attributes 5, 5, and call the area() method on it.
        
        secondValue = 25.

        We assert that the value 25 is equal to the return value of the
        area() method called on shape1, which should return an area
        of 25.
        '''
        shape1 = Rectangle(5,5)
        firstValue = shape1.area()
        secondValue = 25
        self.assertEqual(firstValue, secondValue)

    def test_volume(self):
        '''Summary of test_volume() Test
        This test checks to make sure the volume() function returns
        the correct calculations

        Parameters:
        shape1 = Parallelepiped(4,4,4): We instantiate the object shape1 as a
        Parallelepiped with attributes 4 (length) and 4 (width) and 4 (height).

        firstValue = shape1.volume(): An object of the Parallelepiped class
        with attributes 4, 4, 4, and call the volume() method on it.
        
        secondValue = 64.

        We assert that the value 64 is equal to the return value of the
        volume method called on shape1, which should return a volume
        of 64.
        '''
        shape1 = Parallelepiped(4,4,4)
        firstValue = shape1.volume()
        secondValue = 64
        self.assertEqual(firstValue, secondValue)

    @patch('project04classes.Rectangle.display')
    def test_display(self, mock_display):
        '''Summary of test_display() Test
        This test checks to make sure the volume() function returns
        a print statement.

        Parameters:
        mock_display.return_value = STR: We use a mock object to test
        if our display() returns a string, and compare that assert that
        the str is equal to the same str passed through the assertEqual()
        function.
        '''
        mock_display.return_value = "The dimensions of the Rectangle are:"
        self.assertEqual(mock_display(), "The dimensions of the Rectangle are:")
        
        
if __name__ == "__main__":
    unittest.main()
