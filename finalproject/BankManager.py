from Bank import *
from BankUtility import *
from Account import *

class BankManager:
    def __init__(self):
        self.bank = Bank()

        run = True
        while run:
            print(f'''============================================================
What do you want to do?
1. Open an account
2. Get account information and balance
3. Change PIN
4. Deposit money in account
5. Transfer money between accounts
6. Withdraw money from account
7. ATM withdrawal
8. Deposit change
9. Close an account
10. Add monthly interest to all accounts
11. End Program
============================================================ ''')
            menu_item = input("Enter #: ")
            try:
            
                # For ending program
                if options(menu_item) == 11:
                    run = False
                    break
                # For adding an account
                elif options(menu_item) == 1:
                    self.bank.openAccount()
                # For displaying the account information    
                elif options(menu_item) == 2:
                    BankManager.promptForAccountNumberAndPIN(self.bank)
        

                    pass
                elif menu_item == 3:
                    pass
                elif menu_item == 4:
                    pass
                elif menu_item == 5:
                    pass
                elif menu_item == 6:
                    pass
                elif menu_item == 7:
                    pass
                elif menu_item == 8:
                    pass
                elif menu_item == 9:
                    pass
                elif menu_item == 10:
                    pass
            except TypeError: "Please enter a number"
# 07432795
# 5318        
        
        # This is where you will implement your ‘main’ method and start
        # the program from.  The BankManager class should create an instance
        # of a Bank object when the program runs and use that instance to
        # manage the Accounts in the bank

       
    @staticmethod    
    def promptForAccountNumberAndPIN(bank):
        acct = input("Enter account number:\n")
        pin = input("Enter PIN number:\n")
        if pin.isValidPIN(pin):
            return acct, pin   
        else:
            print("Please enter a valid PIN.")      
              

        
        
        # implement promptForAccountNumberAndPIN here
        # takes one parameter, a Bank object that represents the bank.
        # The method should prompt the user to enter an account number
        # and then try to find a matching account with that account number
        # in the bank.
        
         # be sure to change this as needed

def options(selection):
    '''Summary of OPTIONS Function:
    This function validates the users input
    
    Parameters:
    selection(str): Selection should be input entered via input() function.

    Returns: INT in range 1-4, corresponding with the 4 menu items
    '''
    try:
        selection = int(selection)
        if selection in range(1,11):
            return selection
    except TypeError:
        return input('ERROR: Please enter a number. \nPress Enter to Continue.')
    except ValueError:
        return input('ERROR: Please enter a number in the range of 1-4. \nPress Enter to Continue.')
