# Assignment 4 Write Up
This program prompts the user for input for the dimensions of shapes, specifically a rectangle and a parallelepiped, and returns the dimensions of those shapes.

# Assignment 4 Algorithm
1. First, we create the Rectangle class.
2. We then create methods for this class - an area() and perimeter() method to return the afformentioned calculations, and then a display() method to print the dimensions of the object in the class Rectangle.
3. Next, we create a Parallelepiped class.
4. We then create methods for this class - a volume() methond to return the afformentioned calculations, and a display() method to print the dimensions of the object in the class Parallelepiped. We also inherit the appropiate methods to help with our calculations.
5. Then we create a validEntry function that determines whether the user successfully entered an INT or a FLOAT, and returns FALSE otherwise.
6. If user unsuccessfully enters the appropriate input, we should keep prompting the user until successful.
7. Once the user succesfully enters the correct input, we instatiate a class of the appropriate shape, with the users input passed through as attributes.
8. Lastly, we call the appropriate methods, area(), perimeter(), and volume() on our shapes, followed by the display() method to print the dimensions of the shapes.
