from Account import *
from Bank import *

class Bank:
    def __init__(self) -> None:
        self.accounts = []
        self.accountsLimit = 2
    

    def addAccountToBank(self,newAccount):
        '''This function takes in a new account as a parameter
        and appends it to our list of bank accounts'''
        if len(self.accounts) >= self.accountsLimit:
            print("No more accounts available")
            return False # be sure to change this as needed
        else:
            return True, self.accounts.append(newAccount)
            

    def removeAccountFromBank(self, account_num):
        account = self.findAccount(account_num)
        self.accounts.remove(account)

  
    def findAccount(self, account_num):
        '''This function finds the matching account in the 
        bank account list and returns it'''
        for account in self.accounts:
            if account.getAccountNumber() == account_num:
                return account
        return "Searched element not in the list"

    def addMonthlyInterest(percent):
        pass
        # EXTRA CREDIT


    def openAccount(self):
        print("OPEN ACCOUNT")
        newAccount = Account()
        fName = input("Enter Account Owner's First Name:\n")
        lName = input("Enter Account Owner's Last Name:\n")
        ssn_input = input("Enter Account Owner's SSN (9 digits):")
        newAccount.setFirstName(fName)
        newAccount.setLastName(lName)
        newAccount.setSSN(ssn_input)
        newAccount.genPin()
        newAccount.genAccNum()
        newAccount.display()
        self.addAccountToBank(newAccount)
        cont = input("Press Enter to Continue ")
