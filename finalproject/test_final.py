from Account import *
from Bank import *
from BankManager import *
from BankUtility import *
from CoinCollector import *
import unittest

class FinalProject(unittest.TestCase):

    def testCoinCollecter1(self):
        '''
        '''
        bal = CoinCollector.parseChange("PNDQHW")

        self.assertEqual(str(bal),"1.91")

    def testCoinCollecter2(self):
        '''This test...
        '''
        bal = CoinCollector.parseChange("PNDQHW")

        self.assertEqual(str(bal),"1.91")

    def testCoinCollecter3(self):
        '''This test...
        '''
        pass

    def testDeposit1(self):
        '''This test...
        '''
        pass
    
    def testDeposit2(self):
        '''This test...
        '''
        pass

    def withdraw1(self):
        '''This test...
        '''
        pass

    def withdraw2(self):
        '''This test...
        '''
        pass

    def isValidPIN1(self):
        '''This test...
        '''
        pass

    def isValidPIN2(self):
        '''This test...
        '''
        pass

    def addAccountToBank1(self):
        '''This test...
        '''
        pass
    
    def addAccountToBank2(self):
        '''This test...
        '''
        pass
    
    def removeAccountFromBank1(self):
        '''This test...
        '''
        pass

    def removeAccountFromBank2(self):
        '''This test...
        '''
        pass
    
    def findAccount1(self):
        '''This test...
        '''
        pass

    def findAccount2(self):
        '''This test...
        '''
        pass
    
    def addMonthlyInterest1(self):
        '''This test...
        '''
        pass

    def addMonthlyInterest2(self):
        '''This test...
        '''
        pass

    def isNumeric1(self):
        '''This test...
        '''
        pass

    def isNumeric2(self):
        '''This test...
        '''
        pass

    def convertFromDollarsToCents1(self):
        '''This test...
        '''
        pass

    def convertFromDollarsToCents2(self):
        '''This test...
        '''
        pass

    def generateRandomInteger1(self):
        '''This test...
        '''
        pass

    def generateRandomInteger2(self):
        '''This test...
        '''
        pass


if __name__ == "__main__":
    unittest.main()