import random


class Account:
    # add your attributes here
    def __init__(self) -> None:
        self.accountNum = None
        self.firstName = None
        self.lastName = None
        self.ssn = "XXX-XX-"
        self.pin = None
        self.bal = "$0.00"
        pass
    

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

    def setSSN(self,ssn_input):
        self.ssn = ssn_input
        #run = True
        #while run:
        #    ssn_input = input("Enter Account Owner's SSN (9 digits):")
        #    if len(input) == 9:
        #        self.ssn = ssn_input
        #        run = False
        #        break
        #    else:
        #        print("Please try again")

    # deposit and withdraw
    def deposit(self, amount):
        self.bal == self.bal + amount
    def withdraw(self, amount):
        if self.bal < amount:
            self.bal = self.bal - amount
        else: 
            return "Insufficient funds"
    
    def setPin(self):
        first = str(random.randint(0, 9))
        second = str(random.randint(0, 9))
        third = str(random.randint(0, 9))
        fourth = str(random.randint(0, 9))
        self.pin = first+second+third+fourth
    
    def getPin(self):
        return f"PIN #: {self.pin}"

    def setAccountNumber(self):
        base = []
        for x in range(8):
            x = str(random.randint(0,9))
            base.append(x)
        acct = "".join(base)
        self.accountNum = acct
  
    
    def display(self):
        print(f'''============================================================
Account Number: {self.accountNum}
Owner First Name: {self.firstName}
Owner Last Name: {self.lastName}
Owner SSN: {self.ssn}
PIN: {self.pin}
Balance: {self.bal}
============================================================''')
    
    
    def isValidPIN(self, entered_pin):
        if self.pin == entered_pin:
                return True
        return False
    
    
    # all objects have a toString method - this indicates you are providing
    # your own version
    def __repr__(self):
        rep = f'============================================================ \
Account Number: {self.accountNum} \
Owner First Name: {self.firstName} \
Owner Last Name: {self.lastName} \
Owner SSN: {self.ssn} \
PIN: {self.pin} \
Balance: {self.bal} \
============================================================' # change this as needed
        return rep
