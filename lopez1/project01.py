# import PI from MATH to get accurate number for PI
from math import pi

radius = input("Enter the radius: \n")

def circ(x):
    """Summary of Function circ()
    
    Parameters:
    arg1 (int): Radius, input by user
    
    Returns:
    int: Circumference of radius
    """
    return 2 * (pi * x)

def area(x):
    """Summary of Function area()
    
    Parameters:
    arg1 (int): Radius, input by user
    
    Returns:
    int: Area of radius
    """
    return pi * (x**2)

def vol(x):
    """Summary of Function vol()
    
    Parameters:
    arg1 (int): Radius, input by user
    
    Returns:
    int: Volume of radius
    """
    return 4/3 * (pi * (x**3))

# setting run = True and placing the calculation within a while loop
# will allow us to keep the program running if 
# a user does not enter a number and encounters an error
run = True
while run:

    # this try block will attempt to run the calculations
    try:
        radius = float(radius)
        
        # calculate the circumference
        c = circ(radius)
    
        # calculate the area
        a = area(radius)
    
        # calculate the volume
        v = vol(radius)
    
    # this except block will return an error if the user does not enter a number    
    except:
        print('Something went wrong. Did you enter a number?')
        radius = input('Please try again - enter the radius: \n')
    
    # if calculations are successful, we set RUN to FALSE to end while loop and quit program
    else:
        run = False
        print(f'''
The circumference of a circle with a radius of {radius} is {c}. 
The area of a circle with a radius of {radius} is {a}.
The volume of a sphere with a radius of {radius} is {v}.
    ''' )

#print(circ.__doc__)
#print(area.__doc__)
#print(vol.__doc__)