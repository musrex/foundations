from Account import *
from Bank import *

class Bank:
    def __init__(self) -> None:
        self.accounts = []
        self.accountsLimit = 2
    

    def addAccountToBank(self,account_num):
        if len(self.accounts) >= self.accountsLimit:
            print("No more accounts available")
            return False # be sure to change this as needed
        else:
            for account in self.accounts:
                if account == None:
                    return True, self.accounts.append(account)
            

    def removeAccountFromBank(account):
        pass
            # implement removeAccountFromBank here

        #return False; # be sure to change this as needed
  
    def findAccount(self, accountNum):
        for account in self.accounts:
            if accountNum == self.accountNum:
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
        newAccount.setPin()
        newAccount.setAccountNumber()
        newAccount.display()
        self.addAccountToBank(newAccount)
            
        #else:
        #    print('Something went wrong.')
        cont = input("Press Enter to Continue ")