from transports import *
from options import *

mainStation = Terminal()

def main():   
    
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
        selection = input('Enter: ')
        print()

        if selection == "":
            continue
        elif options(selection) == 4:
            run = False
            print('Have a nice day!')
            break  
        elif options(selection) == 3:
            print('''<-W-|-E->''')        
            mainStation.display()
            enter = input('\nPress Enter to Continue')
            print()
        elif options(selection) == 1 or options(selection) == 2:
            answered = False
            while not answered:
                try:
                    transport = int(input('Enter transport ID: '))
                    print()                            

                    if addTransport(options(selection), mainStation, transport):
                        print('Success!')
                        answered = True
                        break          
                except TypeError:
                    input('ERROR: Please enter a number. \nPress Enter to Continue.')
                except ValueError:
                    input('ERROR: Please enter a number. \nPress Enter to Continue.')

if __name__=='__main__':
    main()