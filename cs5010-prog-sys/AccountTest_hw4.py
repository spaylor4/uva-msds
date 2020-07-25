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
    def test_getFee_1(self):
        self.assertEqual(first, second)
        
    def test_getFee_2(self):
        self.assertEqual(first, second)
        
    def test_deposit_1(self):
        self.assertEqual(first, second)
        
    def test_deposit_2(self):
        self.assertEqual(first, second)
        
    def test_withdraw_1(self):
        self.assertEqual(first, second)
        
    def test_withdraw_2(self):
        self.assertEqual(first, second)
            














