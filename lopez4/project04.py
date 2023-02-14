from project04classes import *

def validEntry(input):
    '''Summary of validEntry() Function
    This function tests whether the input entered by a
    user is valid for mathematical calculations. The function
    determines whether the input can be converted to an int()
    or a float(), and then returns the appropriate type.
    If it can't be converted, the function returns FALSE

    Parameters:
    input (str): This str() is entered by the user using the INPUT function.

    Returns:
    int, float, or FALSE.
    int: If the users input can be succesfully converted to an int.
    float: If the users input can be succesfully converted to a float.
    FALSE: If the users input cannot be converted to either an int or float.
    '''
    input = str(input)
    try:
        if "." in input:
            input = float(input)
            return(input)
        else:
            input = int(input)
            return(input)
    except:
        return False

if __name__ == "__main__":

    print("Calculate the Dimensions of a Rectangle")

    validLength = False
    while not validLength:
        length = input("Enter the length: ")
        length = validEntry(length)
        if validEntry(length) != False:
            validLength = True
            break
        else:          
            print("Please enter a number.")

    validWidth = False
    while not validWidth:
        width = input("Enter the width: ")
        width = validEntry(width)
        if validEntry(width) != False:
            validWidth = True
            break
        else:
            print("Please enter a number.")

    shape1 = Rectangle(length, width)
    print()
    shape1.display()

    print("Calculate the Dimensions of a Parallelepiped.")

    validLength = False
    while not validLength:
        length = input("Enter the length: ")
        length = validEntry(length)
        if validEntry(length) != False:
            validLength = True
            break
        else:          
            print("Please enter a number.")

    validWidth = False
    while not validWidth:
        width = input("Enter the width: ")
        width = validEntry(width)
        if validEntry(width) != False:
            validWidth = True
            break
        else:
            print("Please enter a number.")

    validHeight = False
    while not validHeight:
        height = input("Enter the height: ")
        height = validEntry(height)
        if validEntry(width) != False:
            validHeight = True
            break
        else:
            print("Please enter a number.")

    shape2 = Parallelepiped(length, width, height)
    print()
    shape2.display()
