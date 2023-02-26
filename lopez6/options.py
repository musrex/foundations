def options(selection):
    '''Summary of OPTIONS Function:
    This function validates the users input
    
    Parameters:
    selection(str): Selection should be input entered via input() function.

    Returns: INT in range 1-4, corresponding with the 4 menu items
    '''
    try:
        selection = int(selection)
        if selection in range(1,5):
            return selection
    except TypeError:
        return input('ERROR: Please enter a number. \nPress Enter to Continue.')
    except ValueError:
        return input('ERROR: Please enter a number in the range of 1-4. \nPress Enter to Continue.')

def addTransport(direction, terminal):
    '''Summary of ADDTRANSPORT Function:
    This function adds a transport to a terminal

    Parameters:
    direction(function): The direction function returns an INT in the range of 1-4.
    This INT determines the direction the transport came from, and which on of the
    deque it will enter.

    terminal(Class): This terminal is our deque the transport will be added to.

    Returns:
    '''
    answered = False
    while not answered:
        try:
            transport = int(input('Enter transport ID: '))
            print()
            if direction == 1:
                terminal.west(str(transport))
                print('Success!')
                answered = True
                break
            elif direction == 2:
                terminal.east(str(transport))
                answered = True
                print('Success!')
                break
        except TypeError:
            input('ERROR: Please enter a number. \nPress Enter to Continue.')
        except ValueError:
            input('ERROR: Please enter a number. \nPress Enter to Continue.')