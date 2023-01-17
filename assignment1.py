# import PI from MATH to get accurate number for PI
from math import pi

radius = input("Enter the radius: \n")

# setting run = True and placing the calculation within a while loop
# will allow us to keep the program running if 
# a user does not enter a number and encounters an error
run = True
while run:

    # this try block will attempt to run the calculations
    try:
        radius = float(radius)
        
        # calculate the circumference
        c = 2 * (pi * radius)
    
        # calculate the area
        a = pi * (radius**2)
    
        # calculate the volume
        v = 4/3 * (pi * (radius**3))
    
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