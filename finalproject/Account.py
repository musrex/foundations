import random
from BankUtility import *

class Account:
    def __init__(self) -> None:
        self.accountNum = None
        self.firstName = None
        self.lastName = None
        self.ssn = None
        self.pin = None
        self.bal = "$0.00"
        
    # generate pin number        
    def genPin(self):
        a = str(BankUtility.generateRandomInteger(0, 9))
        b = str(BankUtility.generateRandomInteger(0, 9))
        c = str(BankUtility.generateRandomInteger(0, 9))
        d = str(BankUtility.generateRandomInteger(0, 9))
        self.pin = a+b+c+d
    
    # generate account number
    def genAccNum(self):
        a = str(BankUtility.generateRandomInteger(0, 9))
        b = str(BankUtility.generateRandomInteger(0, 9))
        c = str(BankUtility.generateRandomInteger(0, 9))
        d = str(BankUtility.generateRandomInteger(0, 9))
        e = str(BankUtility.generateRandomInteger(0, 9))
        f = str(BankUtility.generateRandomInteger(0, 9))
        g = str(BankUtility.generateRandomInteger(0, 9))
        h = str(BankUtility.generateRandomInteger(0, 9))
        self.accountNum = a+b+c+d+e+f+g+h
    

    # getters for first and last name
    def getFirstName(self):
        return self.firstName
    
    def getLastName(self):
        return self.lastName

    # setters for first and last name
    def setFirstName(self, fname):
        self.firstName = fname

    def setLastName(self, lname):
        self.lastName = lname

    # getters and setters for SSN
    def setSSN(self,ssn_input):
        self.ssn = ssn_input

    def getSSN(self):
        return "XXX-XX-" + self.ssn[5:]

    # return the account balance
    def getBal(self):
        return self.bal

    # deposit and withdraw
    def deposit(self, amount):
        if self.bal == "$0.00":
            self.bal = 0
            self.bal = self.bal + amount
        else:
            self.bal = self.bal + amount

    # withdraw money from account
    def withdraw(self, amount):
        if self.bal == "$0.00":            
            self.bal = 0
            return False
        elif self.bal > amount:
                self.bal = self.bal - amount
        else: 
            return False

    # getters and setters for PIN
    def setPin(self, pin_num):
        self.pin = pin_num

    def getPin(self):
        return f"PIN #: {self.pin}"

    # getters and setters for account number
    def setAccountNumber(self):
        base = []
        for x in range(8):
            x = str(random.randint(0,9))
            base.append(x)
        acct = "".join(base)
        self.accountNum = acct

    def getAccountNumber(self):
        return self.accountNum

    # a function that displays account info
    def display(self):
        print(f'''============================================================
Account Number: {self.accountNum}
Owner First Name: {self.firstName}
Owner Last Name: {self.lastName}
Owner SSN: {self.getSSN()}
PIN: {self.pin}
Balance: {self.bal}
============================================================''')
    
    # checks to make sure PIN is valid
    def isValidPIN(self, entered_pin):
        if int(entered_pin) == int(self.pin):
                return True
        return False
    
    # a function that returns account info as a string variable, similar to display()
    def toString(self):
        string = f'''============================================================
Account Number: {self.accountNum}
Owner First Name: {self.firstName}
Owner Last Name: {self.lastName}
Owner SSN: {self.getSSN()}
PIN: {self.pin}
Balance: {self.bal}
============================================================'''
        return string
