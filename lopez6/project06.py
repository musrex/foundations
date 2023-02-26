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
        elif options(selection) in range(1,3):
            addTransport(options(selection), mainStation)
        elif options(selection) == 3:
            print('''<-W-|-E->''')        
            mainStation.display()
            enter = input('\nPress Enter to Continue')
            print()
        elif options(selection) == 4:
            run = False
            print('Have a nice day!')
            break            

if __name__=='__main__':
    main()