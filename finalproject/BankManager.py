from Bank import *
from BankUtility import *
from Account import *
from CoinCollector import *


def options():
    '''Summary of OPTIONS Function:
    This function validates the users input
    
    Parameters:
    selection(str): Selection should be input entered via input() function.

    Returns: INT in range 1-11, corresponding with the 11 menu items
    '''
    try:
        selection = input("Enter #: ")
        selection = int(selection)
        if selection in range(1,11):
            return selection
    except:
        input('ERROR: Please enter a number in the range of 1-11. \nPress Enter to Continue.')


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
            
                # For ending program
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
                    BankManager.depositMoney(bank)
                elif selection == 5:
                    BankManager.transferMoney(bank)
                elif selection == 6:
                    BankManager.withdrawMoney(bank)
                elif selection == 7:
                    BankManager.atmWithdraw(bank)
                elif selection == 8:
                    BankManager.depositChange(bank)
                elif selection == 9:
                    BankManager.closeAccount(bank)
                elif selection == 10:
                    BankManager.monthlyInterest(bank)
            except TypeError: "Please enter a number"

        
        # This is where you will implement your ‘main’ method and start
        # the program from.  The BankManager class should create an instance
        # of a Bank object when the program runs and use that instance to
        # manage the Accounts in the bank

    def cont():
        input('Press Enter to continue.\n')

    @staticmethod    
    def promptForAccountNumberAndPIN(bank):
        '''This function takes in a bank object, prompts a user for Account
        number and PIN, and returns the appropriate account.'''
        account_num = input("Enter account number:\n")
        account = bank.findAccount(account_num)

        try:
            if account is not None:
                pin = input("Enter PIN number:\n")
                if account.isValidPIN(pin):
                    return account   
            else:
                print("Please enter a valid PIN.")
                return False      
        except:       
            print(f"Account not found for account number: {account_num}")
            BankManager.cont()
            return False
        

    def changePin(bank):
        '''This function takes in a bank object, and prompts the user
        for a new PIN so that they may change their PIN.'''
        account = BankManager.promptForAccountNumberAndPIN(bank)
        if account is not False:
            run = True
            while run:
                newPin = input("Enter new PIN: ")
                if BankUtility.isNumeric(newPin) and len(newPin) == 4:
                    confirm = input("Enter new PIN again to confirm:\n")
                    if newPin == confirm:
                        account.setPin(newPin)
                        print("PIN updated")
                        run = False
                        break
                else:
                    input("Please enter a valid PIN \nPress Enter to Continue.")

    def depositMoney(bank):
        '''This function takes in a bank object, prompts the user for a deposit in 
        dollars and cents so that they may make a deposit on their account.'''
        account = BankManager.promptForAccountNumberAndPIN(bank)
        if account is not False:
            run = True
            while run:
                deposit = input("Enter amount to deposit in dollars and cents (e.g. 2.57):\n")
                try:
                    if float(deposit) <= 0:
                        print("Amount cannot be negative. Try again")
                    else:
                        deposit = float(deposit)
                        account.deposit(deposit)
                        print(f"New balance:${account.getBal()}")
                        BankManager.cont()
                        run = False
                        break
                except:
                    print("Error")

    def transferMoney(bank):
        '''This function takes in a bank object, and then prompts the user for the
        information for two '''
        account1 = BankManager.promptForAccountNumberAndPIN(bank)
        if account1 is not False:            
            account2 = BankManager.promptForAccountNumberAndPIN(bank)
            if account2 is not False:
                run = True
                while run:
                    transfer = input("Enter amount to transfer in dollars and cents (e.g. 2.57):\n")
                    transfer = float(transfer)
                    try:
                        if transfer <= 0:
                            print("Amount cannot be negative. Try again")
                        else:
                            account1.withdraw(transfer)
                            account2.deposit(transfer)
                            print(f'''Transfer Complete
New balance in account:{account1.getAccountNumber()} is:${account1.getBal()}
New balance in account:{account2.getAccountNumber()} is:${account2.getBal()}''')
                            BankManager.cont()
                            run = False
                            break
                    except:     
                        print("Error")

    def withdrawMoney(bank):
        '''This function takes in a bank object, prompts the user for a withdrawal in 
        dollars and cents so that they may make a deposit on their account.'''
        account = BankManager.promptForAccountNumberAndPIN(bank)
        if account is not False:
            run = True
            while run:
                withdraw = input("Enter amount to withdraw in dollars and cents (e.g. 2.57):\n")
                withdraw = float(withdraw)
                try:
                    if withdraw <= 0:
                        print("Amount cannot be negative. Try again")
                    else:
                        account.withdraw(withdraw)
                        print(f"New balance:${account.getBal()}")
                        BankManager.cont()
                        run = False
                        break
                except:
                    print("Error")
    
    def atmWithdraw(bank):
        account = BankManager.promptForAccountNumberAndPIN(bank)
        if account is not False:
            run = True
            while run:
                withdraw = input("Enter amount to withdraw in dollars (no cents) in multiples of $5 (limit $1000):\n")
                withdraw = float(withdraw)
                try:
                    if withdraw > 1000 or withdraw < 5 or withdraw % 5 != 0:
                        print("Invalid amount. Try again.")
                        BankManager.cont()
                    else:    
                        if account.withdraw(withdraw) is not False:
                            twenties = withdraw // 20
                            tens = (withdraw - (20 * twenties) ) // 10
                            fives = (withdraw - ((20 * twenties)+(10 * tens)) ) // 5
                            print(f'''Number of 20-dollar bills:{int(twenties)}
Number of 10-dollar bills:{int(tens)}
Number of 5-dollar bills:{int(fives)}
New balance: ${account.getBal()} ''')
                            BankManager.cont()
                            run = False
                            break
                        else:
                            print("Insufficient funds")
                            run = False
                            break    
                except:
                    print("Error")        
        

    def depositChange(bank):
        account = BankManager.promptForAccountNumberAndPIN(bank)
        if account is not False:
            change = input("Deposit coins: \n")
            print(CoinCollector.parseChange(change))

    def closeAccount(bank):
        account = BankManager.promptForAccountNumberAndPIN(bank)
        if account is not False:
            print(f"Account {account.getAccountNumber()} closed")
            pass
    
    def monthlyInterest(bank):
        pass
