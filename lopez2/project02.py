run = True


def evenly(a=int, b=int):
    if int(a) % int(b) == 0 or int(b) % int(a) == 0:
        return(True)
    else:
        return(False)


while run == True:
    print("Please enter two numbers to see if either evenly divides the other.")
    a = input("First number: ")
    b = input("Second number: ")


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


    except:
        print(
            '''
Something went wrong. Did you enter a number?
Please try again.
            ''')
