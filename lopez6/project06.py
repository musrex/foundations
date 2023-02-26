from transports import *


def main():
    
    mainStation = Terminal()
    print('''
Welcome to the Central Terminal!
What would you like to do?
Use the menu below to navigate.
------------------------------''')
    

    # keeps our program running
    run = True
    while run:
        print('''Enter the number corresponding 
to the menu item.
------------------------
1. Add Western Transport
2. Add Eastern Transport
3. See All Transports
4. Quit
''')
        option = input('Enter: ')
        print()
        # we put the majority of our code
        # in this try block so that we
        # have a way to deal with invalid entrys
        try:
            if option == '4':
                run = False
                print('Have a nice day!')
                break
            elif option == '3':
                print('''<-W-|-E->
---------''')
                mainStation.display()
                enter = input('\nPress Enter to Continue')
                print()
            elif option == '1':
                answered = False
                while not answered:
                    transport = input('Enter transport ID: ')
                    print()
                    
                    # another try block
                    # but this time we try to 
                    # convert their input into
                    # a string as a way to 
                    # validate entries,
                    # and then just convert 
                    # transport back str 
                    # upon append.
                    try:
                        transport = int(transport)
                        mainStation.west(str(transport))
                        answered = True
                        break
                    except:
                        print('ERROR: ENTER NUMBER')
            elif option == '2':
                answered = False
                while not answered:
                    transport = input('Enter transport ID: ')
                    print()
                    try:
                        transport = int(transport)
                        mainStation.east(str(transport))
                        answered = True
                        break
                    except:
                        print('ERROR: ENTER NUMBER')
        except:
            print('Please enter a number.')
        #answered = False
        #while not answered:
        #    eastUnits = input('Do we have transports from the east? ')
        #    westUnits = input('Do we have transports from the west? ')
#
        #    mainStation.east(eastUnits)
        #    mainStation.west(westUnits)
#
        #    result = mainStation.size()
#
        #stack.display()
        #print(result)

main()