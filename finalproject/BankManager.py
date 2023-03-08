from Bank import *
from BankUtility import *
from Account import *



def options():
    '''Summary of OPTIONS Function:
    This function validates the users input
    
    Parameters:
    selection(str): Selection should be input entered via input() function.

    Returns: INT in range 1-4, corresponding with the 4 menu items
    '''
    try:
        selection = input("Enter #: ")
        selection = int(selection)
        if selection in range(1,11):
            return selection
    except:
        input('ERROR: Please enter a number in the range of 1-4. \nPress Enter to Continue.')


class BankManager:
    def __init__(self):
        bank = Bank()

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
            selection = options()
            try:
            
                # For ending program 32191678 13123
                if selection == 11:
                    run = False
                    break
                # For adding an account
                elif selection == 1:
                    bank.openAccount()
                    
                # For displaying the account information    
                elif selection == 2:
                    account = BankManager.promptForAccountNumberAndPIN(bank)
                    print(account.toString())
                    cont = input("Press Enter to Continue ")
                elif selection == 3:
                    BankManager.changePin(bank)
                elif selection == 4:
                    pass
                elif selection == 5:
                    pass
                elif selection == 6:
                    pass
                elif selection == 7:
                    pass
                elif selection == 8:
                    pass
                elif selection == 9:
                    pass
                elif selection == 10:
                    pass
            except TypeError: "Please enter a number"
      
        
        # This is where you will implement your ‘main’ method and start
        # the program from.  The BankManager class should create an instance
        # of a Bank object when the program runs and use that instance to
        # manage the Accounts in the bank

       
    @staticmethod    
    def promptForAccountNumberAndPIN(bank):
        account = input("Enter account number:\n")
        account = bank.findAccount(account)

        if account is not None:
            pin = input("Enter PIN number:\n")
            if account.isValidPIN(pin):
                return account   
        else:
            print("Please enter a valid PIN.")      
              

        
        
        # implement promptForAccountNumberAndPIN here
        # takes one parameter, a Bank object that represents the bank.
        # The method should prompt the user to enter an account number
        # and then try to find a matching account with that account number
        # in the bank.
        
         # be sure to change this as needed

    
    def changePin(bank):
        account = BankManager.promptForAccountNumberAndPIN(bank)
        run = True
        while run:
            newPin = input('Enter new PIN: ')
            if BankUtility.isNumeric(newPin) and len(newPin) == 4:
                confirm = input("Enter new PIN again to confirm:\n")
                if newPin == confirm:
                    account.setPin(newPin)
                    print('PIN updated')
                    run = False
                    break
            else:
                input("Please enter a valid PIN \nPress Enter to Continue.")

