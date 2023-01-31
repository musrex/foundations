def evenly(a=int, b=int):
    """Summary of Function evenly()
    Checks to see if arg1 and arg2 can be evenly divided be the other

    Parameters:
    arg1 (int): First input
    arg2 (int): Second input
    
    Returns:
    boolean: True if either parameter is evenly divided by the other
    """
    if int(a) % int(b) == 0 or int(b) % int(a) == 0:
        return(True)
    else:
        return(False)

# setting run = True and calling evenly() within a while loop
# will allow us to keep the program running if 
# a user does not enter a number and encounters an error
run = True
while run == True:
    print("Please enter two numbers to see if either evenly divides the other.")
    a = input("First number: ")
    b = input("Second number: ")

    # this try block will attempt to call the evenly() function
    try:
        result = evenly(a,b)
        if result == True:
            run = False
            print('\n'+str(result))
        else:
            print(f'''
{result}
These numbers do not evenly divide. Please try again.
            ''')

    # this except block will return an error if the user does not enter a number
    except:
        print(
            '''
Something went wrong. Did you enter a number?
Please try again.
            ''')
