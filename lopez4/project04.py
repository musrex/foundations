class Rectangle:
    '''
    Words go here
    '''
    #  we use the __init__ method initiate the class as soon as it's called.
    # for instance, as soon r1 = Rectangle(2,4) is declared, that object with those
    # attributes is created.
    def __init__(self, length, width):
        self.length = length 
        self.width = width

    # this bit of code that looks like a function is actually a method
    # a function is called like so: perimeter(square)
    # a method is called on something like so: square.perimeter() 
    def perimeter(self):
        '''Summary of perimeter() method
        This method can be called on objects of the Rectangle class to 
        return the perimeter of the object.
        ''' 
        perimeter = (self.length * 2) + (self.width * 2)
        return perimeter

    def area(self):
        '''Summary of area() method
        This method can be called on objects of the Rectangle class to 
        return the area of the object.
        ''' 
        area = self.length * self.width
        return area

    def display(self):
        '''Summary of display() method
        This method can be called on objects of the Rectangle class to 
        print the dimensions of the object.
        ''' 
        print(f'''The dimensions of the Rectangle are:
Length = {self.length}
Width = {self.width}
Area = {self.area()}
Perimeter = {self.perimeter()}
''')
    
class Parallelepiped(Rectangle):
    # with this child class, we need to make sure we call the attributes we need,
    # but if attributes are already part of the parent class, we use the below 
    # super() function to correctly reference them from the parent class.
    def __init__(self, length, width, height):
        # we use super() function to bring reference the attributes from the parent class
        super().__init__(length, width)
        self.height = height

    def volume(self):
        '''Summary of volume() method
        This method can be called on objects of the Parallelepiped class to 
        return the volume of the object.
        ''' 
        volume = self.length * self.width * self.height
        return volume

    def display(self):
        '''Summary of display() method
        This method can be called on objects of the Parallelepiped class to 
        print the dimensions of the object.
        ''' 
        print(f'''The dimensions of the Parallelepiped are:
Length = {self.length}
Width = {self.width}
Height = {self.height}
Volume = {self.volume()}
''')

r1 = Rectangle(4, 5)
r2 = Parallelepiped(4,5,6)
r1.display()
r2.display()
