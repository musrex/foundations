from Account import *
from Bank import *

import random

class BankUtility:
    
    def __init(self):
        pass
        
    def promptUserForString(prompt):
        # implement promptUserForString here
        try:
            answer = input(prompt)
            return answer
        except ValueError:
            return "Please enter a string."        

    def promptUserForPositiveNumber(prompt):
        try:
            return int((float(input(prompt))) * 10)  
        except ValueError:
            return "Amount cannot be negative.  Try again"
        # implement promptUserForPositiveNumber here
        
        return 0.0 # be sure to change this
    
    def generateRandomInteger(min, max):
        return random.randint(min, max)
    
    def convertFromDollarsToCents(amount):    
        return int(amount * 100)
    
    '''
      Checks if a given string is a number (long)
      This does NOT handle decimals.
      
      YOU DO NOT NEED TO CHANGE THIS METHOD
      THIS IS FREE FOR YOU TO USE AS NEEDED
      
      @param numberToCheck String to check
      @return true if the String is a number, false otherwise
     '''
    def isNumeric(numberToCheck):
        try:
            if numberToCheck.isdigit():
                return True
            else:
                return False
        except ValueError:
            return False

