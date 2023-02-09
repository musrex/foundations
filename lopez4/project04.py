class Rectangle:
    
    def __init__(self, length, width):
        self.length = length 
        self.width = width

    def perimeter(self):
        perimeter = (self.length * 2) + (self.width * 2)
        return perimeter

    def area(self):
        area = self.length * self.width
        return area

    def display(self):
        print(f'''The dimensions of the Rectangle are:
Length = {self.length}
Width = {self.width}
Area = {self.area()}
Perimeter = {self.perimeter()}
''')
    
#class Parallelepiped(Rectangle):
#    super()__init__.length = length
#    super()__init__.width = width
#    self.height = height
#
#    def volume(self):
#        volume = self.length * self.width * self.height
#        return volume


r1 = Rectangle(4, 5)
#r2 = Parallelepiped(2,4,4)
r1.display()
#r2.display()
