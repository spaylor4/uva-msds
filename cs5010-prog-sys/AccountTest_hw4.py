#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Homework 4: Testing and Debugging
Shannon Paylor
sep4hy
"""

import unittest

#import Account and Checking classes
class Account:
    
    #constructor
    def __init__(self, accountNumber, balance):
        self.accountNumber = accountNumber
        self.balance = balance
        
    #to-string method
    def __str__(self):
        acc_str = "Account number " + str(self.accountNumber)
        bal_str = "Balance: " + str(self.balance)
        return acc_str + "\n" + bal_str
    
#create derived class for checking accounts
class Checking(Account):
    def __init__(self, accountNumber, balance, fee):
        Account.__init__(self, accountNumber, balance) #call base class constructor
        self.fee = fee #initialize params specific to checking class
        
    def __str__(self):
        base_str = Account.__str__(self) #call base class to-string method
        return "Account type: Checking\n" + base_str #append header for checking accounts to base to-string method
    
    #create method to return fee for checking account
    def getFee(self):
        return self.fee
    
    #create deposit method to add money to account
    def deposit(self, amount):
        self.balance = self.balance + amount
        
    #create method to withdraw money from account
    def withdraw(self, amount):
        if amount  + self.fee > self.balance: #check that account has enough money to withdraw
            print("Insufficient funds!")
        else:
            self.balance = self.balance - amount - self.fee
            #withdraw the money if there is enough in the account

#write unit tests
            
class TestAccount(unittest.TestCase):
    def test_init_balance(self):
        my_checking = Checking("123", 2000, 3)
        
        self.assertEqual(my_checking.balance, 2000)
        
    def test_init_account_num(self):
        my_checking = Checking("123", 2000, 3)
        
        self.assertEqual(my_checking.accountNumber, "123")
    
    def test_getFee_1(self):
        my_checking = Checking("123", 2000, 3)
        my_fee = my_checking.getFee()
        
        self.assertEqual(my_fee, 3)
        
    def test_getFee_2(self):
        my_checking = Checking("345", 5000, 0.5)
        my_fee = my_checking.getFee()
        
        self.assertEqual(my_fee, 0.5)
        
    def test_deposit_1(self):
        my_checking = Checking("123", 2000, 3)
        my_checking.deposit(1000)
        my_checking.deposit(1000)
        
        self.assertEqual(my_checking.balance, 4000)
        
    def test_deposit_2(self):
        my_checking = Checking("345", 5000, 0.5)
        my_checking.deposit(100.5)
        my_checking.deposit(100.25)
        
        self.assertEqual(my_checking.balance, 5200.75)
        
    def test_withdraw_sufficient_funds(self):
        my_checking = Checking("123", 2000, 3)
        my_checking.withdraw(1000)
        
        self.assertEqual(my_checking.balance, 997)
        
    def test_withdraw_insufficient_funds(self):
        my_checking = Checking("123", 2000, 3)
        my_checking.withdraw(2000)
        
        self.assertEqual(my_checking.balance, 2000)
            
if __name__ == '__main__':
    unittest.main()













