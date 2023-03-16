from Account import *
from Bank import *
from BankManager import *
from BankUtility import *
from CoinCollector import *
import unittest

bank = Bank()
bank2 = Bank()
testAccount1 = Account()
testAccount1.setPin(1234)

testAccount2 = Account()

class FinalProject(unittest.TestCase):

    def test_CoinCollecter1(self):
        '''This test checks to make sure our string, with the appropriate
        characters representing coins, equals the value those coins would total.
        '''
        bal = CoinCollector.parseChange("PNDQHW")

        self.assertEqual(str(bal),"1.91")

    def test_CoinCollecter2(self):
        '''This test checls to make sure the entered string equals 0.0, meaning
        no valid coins were entered.
        '''
        bal = CoinCollector.parseChange("ERTY")

        self.assertEqual(str(bal),"0.0")

    def test_CoinCollecter3(self):
        '''This test checks to make sure our string, with the appropriate
        characters representing coins, equals the value those coins would total.
        '''
        bal = CoinCollector.parseChange("PPPPPPPPP")

        self.assertEqual(str(bal),"0.09")

    def test_Deposit1(self):
        '''This test makes sure out deposit function works, but depositing 
        a value and checking to see if our account balance then equals that
        value
        '''
        testAccount1.deposit(1234)
        self.assertEqual(testAccount1.getBal(),1234)
    
    def test_Deposit2(self):
        '''This test makes sure out deposit function works, but depositing 
        a value and checking to see if our account balance then equals that
        value
        '''
        testAccount1.deposit(1)
        self.assertEqual(testAccount1.getBal(),1235)

    def test_withdraw1(self):
        '''This test makes sure out withdraw function works, but withdrawing 
        a value and checking to see if our account balance then equals the
        appropriate value.
        '''
        testAccount1.withdraw(1)
        self.assertEqual(testAccount1.getBal(),1234)

    def test_withdraw2(self):
        '''This test makes sure out withdraw function works, but withdrawing 
        a value and checking to see if our account balance then equals the
        appropriate value.
        '''
        testAccount1.withdraw(1233)
        self.assertEqual(testAccount1.getBal(),1)

    def test_isValidPIN1(self):
        '''This test checks to make sure our PIN validation method works
        by asserting that the value passed is True, since we assigned that
        value to our test accounts and know it is a valid PIN.
        '''
        self.assertTrue(testAccount1.isValidPIN(1234))

    def test_isValidPIN2(self):
        '''This test checks to make sure our PIN validation method works
        by asserting that the value passed is False, since we did not assign that
        value to our test accounts and know it is an invalid PIN.
        '''
        self.assertFalse(testAccount1.isValidPIN(4567))

    def test_addAccountToBank1(self):
        '''This test checks to make sure our addAccountToBank method works by 
        adding a test account to a test bank, and then checking that against the 
        length of the bank account list.
        '''
        bank.addAccountToBank(testAccount1)
        self.assertEqual(len(bank.accounts), 1)
    
    def test_addAccountToBank2(self):
        '''This test checks to make sure our addAccountToBank method works by 
        adding a test account to a test bank, and then checking that against the 
        length of the bank account list.
        '''
        bank.addAccountToBank(testAccount2)
        self.assertEqual(len(bank.accounts), 2)
    
    def test_removeAccountFromBank1(self):
        '''This test checks to make sure our removeAccountFromBank method works by 
        removing our test account from our test bank, and then checking that against the 
        length of the bank account list.
        '''
        bank.removeAccountFromBank(testAccount1)
        self.assertEqual(len(bank.accounts), 1)

    def test_removeAccountFromBank2(self):
        '''This test checks to make sure our removeAccountFromBank method works by 
        removing our test account from our test bank, and then checking that against the 
        length of the bank account list.
        '''
        bank.removeAccountFromBank(testAccount2)
        self.assertEqual(len(bank.accounts), 0)
    
    def test_findAccount1(self):
        '''This test checks to make sure our findAccount method works by creating a new
        test account and test bank, setting an account number to that account, and then 
        searching our bank account to see if the account is in there.
        '''
        testAccount3 = Account()
        testAccount3.setAccountNumber()
        bank2.addAccountToBank(testAccount3)
        self.assertTrue(bank.findAccount(testAccount3.getAccountNumber()))

    def test_findAccount2(self):
        '''This test checks to make sure our findAccount method works by creating a new
        test account and test bank, setting an account number to that account, and then 
        searching our bank account to see if the account is in there.
        '''
        testAccount4 = Account()
        testAccount4.setAccountNumber()
        bank2.addAccountToBank(testAccount4)
        self.assertTrue(bank.findAccount(testAccount4.getAccountNumber()))
    
    def test_addMonthlyInterest1(self):
        '''This test checks to see if our monthly interest function works
        by adding the monthly interest to a test account in a test bank, and 
        then comparing that to a value we know would result from the added interest.
        '''
        testAccount5 = Account()
        testAccount5.deposit(2)
        bank2.addAccountToBank(testAccount5)
        bank2.addMonthlyInterest(2.5)

        self.assertEqual(testAccount5.getBal(),2.42)

    def test_addMonthlyInterest2(self):
        '''This test checks to see if our monthly interest function works
        by adding the monthly interest to a test account in a test bank, and 
        then comparing that to a value we know would result from the added interest.
        '''
        testAccount6 = Account()
        testAccount6.deposit(200)
        bank2.addAccountToBank(testAccount6)
        bank2.addMonthlyInterest(2.75)

        self.assertEqual(round(testAccount6.getBal(),2),245.83)

    def test_isNumeric1(self):
        '''This test checks to see if our isNumeric method works by asserting that
        the string "1" is indeed numberic.
        '''
        self.assertTrue(BankUtility.isNumeric("1"))

    def test_isNumeric2(self):
        '''This test checks to see if our isNumeric method works by asserting that
        the string "A" is not numberic.
        '''
        self.assertFalse(BankUtility.isNumeric("A"))

    def test_convertFromDollarsToCents1(self):
        '''This test checks to see if our convertFromDollarsToCents method 
        words but asserting it equal to a value we know to be true.
        '''
        sum = BankUtility.convertFromDollarsToCents(2.75)
        self.assertEqual(sum, 275)

    def test_convertFromDollarsToCents2(self):
        '''This test checks to see if our convertFromDollarsToCents method 
        words but asserting it equal to a value we know to be true.
        '''
        sum = BankUtility.convertFromDollarsToCents(.75)
        self.assertEqual(sum, 75)

    def test_generateRandomInteger1(self):
        '''This test checks to make sure our random number generator works. The min ranges are set so
        that the number generated never equals the number 123.
        '''
        a = BankUtility.generateRandomInteger(2, 9)
        b = BankUtility.generateRandomInteger(3, 9)
        c = BankUtility.generateRandomInteger(4, 9)
        num = a+b+c
        self.assertNotEqual(num, 123)

    def test_generateRandomInteger2(self):
        '''This test checks to make sure our random number generator works. It tests the ranges.
        Because the min range is 1, and max range is 1, all numbers generated should be 1 and equal
        to the number 111.
        '''
        a = BankUtility.generateRandomInteger(1, 1)
        b = BankUtility.generateRandomInteger(1, 1)
        c = BankUtility.generateRandomInteger(1, 1)
        num = str(a)+str(b)+str(c)
        num = int(num)
        self.assertEqual(num, 111)


if __name__ == "__main__":
    unittest.main(buffer=True)