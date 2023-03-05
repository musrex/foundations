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
                if int(menu_item):
                    menu_item = int(menu_item)
                    if menu_item == 11:
                        run = False
                        break
                    elif menu_item == 1:
                        if len(self.bank.accounts) <= self.bank.accountsLimit:
                            for account in self.accounts:
                                if self.accountNum() == account_num:
                                    return self.accounts.append(account)
                        else:
                            print("too many accounts")
                        #3newAccount = Account()
                        #3print("OPEN ACCOUNT")
                        #3fName = input("Enter Account Owner's First Name:\n")
                        #3lName = input("Enter Account Owner's Last Name:\n")
                        #3ssn_input = input("Enter Account Owner's SSN (9 digits):")
                        #3newAccount.setFirstName(fName)
                        #3newAccount.setLastName(lName)
                        #3newAccount.setSSN(ssn_input)
                        #3newAccount.setPin()
                        #3newAccount.setAccountNumber()
                        #3newAccount.display()
                        self.bank.addAccountToBank(newAccount)
                        cont = input("Press Enter to Continue ")
                    elif menu_item == 2:
                        newAccount.display()
                        acct = input("Enter account number:\n")
                        pin = input("Enter PIN number:\n")
                        for accounts in self.bank.accounts:
                            addAccountToBank(acct)

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

        
        
        # This is where you will implement your ‘main’ method and start
        # the program from.  The BankManager class should create an instance
        # of a Bank object when the program runs and use that instance to
        # manage the Accounts in the bank

       
    @staticmethod    
    def promptForAccountNumberAndPIN(bank):
        
        pin = input("Enter PIN: ")
        if pin.isValidPIN():
            pass    
        else:
            print("Please enter a 4 digit PIN.")      
              

        
        
        # implement promptForAccountNumberAndPIN here
        # takes one parameter, a Bank object that represents the bank.
        # The method should prompt the user to enter an account number
        # and then try to find a matching account with that account number
        # in the bank.
        
         # be sure to change this as needed


