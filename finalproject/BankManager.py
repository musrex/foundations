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
        if selection in range(1,12):
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
                    BankManager.getAccountInfo(bank)
                # For changing the PIN
                elif selection == 3:
                    BankManager.changePin(bank)
                # For depositing money in an account
                elif selection == 4:
                    BankManager.depositMoney(bank)
                # Fro transfering money from one account to another
                elif selection == 5:
                    BankManager.transferMoney(bank)
                # For withdrawing money from an account
                elif selection == 6:
                    BankManager.withdrawMoney(bank)
                # For withdrawing cash, in assorted bills, from an account
                elif selection == 7:
                    BankManager.atmWithdraw(bank)
                # For depositing change into an account
                elif selection == 8:
                    BankManager.depositChange(bank)
                # For closing a bank account
                elif selection == 9:
                    BankManager.closeAccount(bank)
                # For adding monthly interest to all accounts    
                elif selection == 10:
                    BankManager.monthlyInterest(bank)
            except TypeError: "Please enter a number"


    def cont():
        '''This function takes in no parameters and simply
        returns an input field asking the user to press Enter.
        This function is meant to slow the print statements so
        a user has time to process the information on the screen
        before going back to the menu'''
        input('Press Enter to continue.\n')

    @staticmethod    
    def promptForAccountNumberAndPIN(bank):
        '''This function takes in a bank object, prompts a user for Account
        number and PIN, and returns the appropriate account.'''
        account_num = input("Enter account number:\n")
        account = bank.findAccount(account_num)
        run = True
        while run:
            try:
                if account is not None:
                    pin = input("Enter PIN number:\n")
                    if not account.isValidPIN(pin):
                        print("Please enter a valid PIN.")
                        BankManager.cont()      
                    else:
                        return account
            except:       
                print(f"Account not found for account number: {account_num}")
                BankManager.cont()
                return False
        
    def getAccountInfo(bank):
        '''This function takes in a bank object, and 
        prompts the user for an account number an pin,
        returning the appropriate bank account information'''
        account = BankManager.promptForAccountNumberAndPIN(bank)
        if account:
            print(account.toString())
            cont = input("Press Enter to Continue ")    

    def changePin(bank):
        '''This function takes in a bank object, and prompts the user
        for a new PIN so that they may change their PIN.'''
        account = BankManager.promptForAccountNumberAndPIN(bank)
        if account is not False:
            run = True
            while run:
                newPin = input("Enter new PIN: ")
                if not BankUtility.isNumeric(newPin):
                    print(f"{newPin} is not a number.")
                elif len(newPin) != 4:
                    print("PIN must be 4 digits, try again.")
                    BankManager.cont()
                else:
                    confirm = input("Enter new PIN again to confirm:\n")
                    if newPin == confirm:
                        account.setPin(newPin)
                        print("PIN updated")
                        run = False
                        break
                    else:
                        print("PINs do not match, try again.")

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
        information for two different accounts, as well as a sum so that the user
        may transfer funds from one account to the other.'''
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
                            if account1.withdraw(transfer):
                                account2.deposit(transfer)
                                print(f'''Transfer Complete
New balance in account:{account1.getAccountNumber()} is:${account1.getBal()}
New balance in account:{account2.getAccountNumber()} is:${account2.getBal()}''')
                                BankManager.cont()
                                run = False
                                break
                            else:
                                print("Insufficient funds")
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
                        if not account.withdraw(withdraw):
                            print(f"Insufficient funds in account {account.getAccountNumber()}")
                            BankManager.cont()
                            run = False
                            break
                        else:
                            print(f"New balance:${account.getBal()}")
                            BankManager.cont()
                            run = False
                            break
                except:
                    print("Error")
    
    def atmWithdraw(bank):
        '''This function takes in a bank object as a parameter and allows our user to 
        withdraw cash in the form of bills - 20s, 10s, and 5s.'''
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
New balance: ${round(account.getBal(),2)} ''')
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
        '''This function uses the parseChange method from the CoinCollecter class
        to take in strings that coincide with coins, adding the appropriate balance
        to an account.'''
        account = BankManager.promptForAccountNumberAndPIN(bank)
        if account is not False:
            change = input("Deposit coins: \n")
            bal = CoinCollector.parseChange(change)
            account.deposit(bal)
            print(f"${bal} in coins deposited into account.")
            print(f"New balance: ${account.getBal()}")
            BankManager.cont()

    def closeAccount(bank):
        '''This function takes in a bank object as a paramter, and then prompts the user
        for an account number and pin. If found, the function removes that account from
        the list, closing it.'''
        account = BankManager.promptForAccountNumberAndPIN(bank)
        if account is not False:
            bank.removeAccountFromBank(account)
            print(f"Account {account.getAccountNumber()} closed")
            BankManager.cont()
    
    def monthlyInterest(bank):
        '''This function prompts the user for input and then uses the
        addMonthlyInterest method to add interest to all accounts
        in the list of accounts'''
        interest = input("Enter annual interest rate percentage (e.g. 2.75 for 2.75%): \n")
        bank.addMonthlyInterest(interest)
        BankManager.cont()
