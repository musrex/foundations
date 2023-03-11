from Account import *
from Bank import *
from BankUtility import *

class Bank:
    def __init__(self) -> None:
        self.accounts = []
        self.accountsLimit = 3
    

    def addAccountToBank(self,newAccount):
        '''This method takes in a new account as a parameter
        and appends it to our list of bank accounts'''
        if len(self.accounts) >= self.accountsLimit:
            print("No more accounts available")
            return False # be sure to change this as needed
        else:
            return True, self.accounts.append(newAccount)
            

    def removeAccountFromBank(self, account_num):
        '''This method takes an account number as a parameter
        and removes it from the list of bank accounts.'''
        account = self.findAccount(account_num)
        self.accounts.remove(account)

  
    def findAccount(self, account_num):
        '''This method finds the matching account in the 
        bank account list and returns it'''
        for account in self.accounts:
            if account.getAccountNumber() == account_num:
                return account
        return "Searched element not in the list"

    def addMonthlyInterest(self, percent):
        '''This method takes in a parameter, yearly interest rate
        and applies it monthly.'''
        try:
            percent = float(percent) / 12
            for account in self.accounts:
                bal = account.getBal() * percent
                bal = round(float(bal), 2)
                account.deposit(bal)
                print(f"Deposited interest:${bal} into account number:{account.getAccountNumber()}, new balance:${account.getBal()}")
        except:
            print("Invalid entry.")
        


    def openAccount(self):
        '''This method opens an account'''
        print("OPEN ACCOUNT")
        newAccount = Account()
        first = False
        while not first: 
            fName = input("Enter Account Owner's First Name:\n")
            if len(fName) != 0:
                first = True
                break
        second = False
        while not second: 
            lName = input("Enter Account Owner's Last Name:\n")
            if len(lName) != 0:
                second = True
                break
        ssn = False
        while not ssn:
            ssn_input = input("Enter Account Owner's SSN (9 digits):")
            if len(ssn_input) == 9:
                if BankUtility.isNumeric(ssn_input):
                    ssn = True
                    break
                else:
                    print("Social Security Number must be 9 digits")
            else:
                print("Social Security Number must be 9 digits")
        newAccount.setFirstName(fName)
        newAccount.setLastName(lName)
        newAccount.setSSN(ssn_input)
        newAccount.genPin()
        newAccount.genAccNum()
        newAccount.display()
        self.addAccountToBank(newAccount)
        cont = input("Press Enter to Continue ")
