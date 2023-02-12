from project04classes import *

print("Calculate the Dimensions of a Rectangle")

def validEntry(input):
    try:
        input = int(input)
        if input > 0:
            return = True, input
    except:
        try:
            input = float(input) 
            if input > 0:
                return = True, input
        except:
            return False


validLength = False
while not validLength:
    length = input("Enter the length: ")
    if validEntry(length) == True
    try:
        length = int(length)
        if length > 0:
            validLength = True
            break
    except:
        try:
            length = float(length) 
            if length > 0:
                validLength = True
                break
        except:
            print("Please enter a number.")

validWidth = False
while not validWidth:
    width = input("Enter the width: ")
    try:
        width = int(width)
        if width > 0:
            validWidth = True
            break
    except:
        try:
            width = float(width)
            if width > 0:
                validWidth = True
                break
        except:
            print("Please enter a number.")

shape1 = Rectangle(length, width)
shape1.display()

print("Calculate the Dimensions of a Parallelepiped.")

validHeight = False
while not validHeight:
    height = input("Enter the height: ")
    try:
        height = int(height)
        if height > 0:
            validHeight = True
            break
    except:
        try:
            height = float(height) 
            if height > 0:
                validHeight = True
                break
        except:
            print("Please enter a number.")

shape2 = Parallelepiped()