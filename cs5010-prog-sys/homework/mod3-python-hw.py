#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Homework: Python
Shannon Paylor
sep4hy
"""

#%%
## Q1: Dictionary Basics
#Create a dictionary of 10 key-value pairs. Choose a domain that interests you. What might you want to look up?
#Demonstrate retrieving at least three different values.
#Display each of the results.

#create dictionary with key golfer name and value number of major championships won
golf_majors_won = {'Jack Nicklaus': 18, 'Tiger Woods': 15, 'Walter Hagen': 11, 'Ben Hogan': 9, 'Gary Player': 9, 
                   'Tom Watson': 8, 'Arnold Palmer': 7, 'Lee Trevino': 6, 'Phil Mickelson': 5, 'Rory McIlroy': 4}

#retrieve and print some results
print(golf_majors_won.get('Rory McIlroy'))
print(golf_majors_won['Phil Mickelson'])
print('Tiger Woods has won ' + str(golf_majors_won['Tiger Woods']) + ' majors.')

#%%
## Q2: Getting User Input
#Ask user for his or her name and two numbers (separately).
#Multiply the two numbers.
#Display an output like the following: Hi, <NAME>! Multiplying <NUM1> and <NUM2> is: <RESULT>
#Display the result as a floating-point number (not an integer).

#get user input for the three values
user_name = input("Please type your name: ")
user_n1 = input("Please type one number: ")
user_n2 = input("Please type another number: ")

#cconvert numbers to float and compute the product
product = float(user_n1) * float(user_n2)

#display the results
print("Hi, " + user_name + "! Multiplying " + str(user_n1) + " and " + str(user_n2) + " is: " + str(product))

#%%
## Q3: Converting code to use a while loop
#Rewrite the guessing game using a while loop (code in pyScript08.py -- Guessing game that asks the user to guess "What is the name of the computer that played on Jeopardy?")
#You may need to use if statements in this solution.
#You may need to use the break statement or the continue statement in this solution
#Remember to mimic the print statements after each try exactly like the original code (therefore, remember to keep track of which try the guesser is on to output the appropriate response).

#setup the game
answer = "Watson"
print("Here is a guessing game. You get three tries.")
print("What is the name of the computer that played on Jeopardy?")
  
#create list of prompts so it can change based on number of guesses remaining       
prompts = ["Enter your guess: ", "Sorry. Guess again: ", "Sorry. One more guess: "]
try_num = 1
while try_num < 4:
    response = input(prompts[try_num - 1]) #python zero-indexed but try_num starts at 1
    if response == answer:
        print("That is right!")
        break #only give them 3 guesses if they're wrong
    try_num += 1
    
if try_num == 4:
    print("Sorry. No more guesses. The answer is " + answer + ".")


#%%
## Q4: Counting Each of the Vowels
#Using ONE for-loop, count the number of each of the vowels in a string (use the following: sentence = "are you suggesting coconuts migrate")
#Display how many a’s, e’s, i’s, o’s, and u’s are in the sentence.

sentence = "are you suggesting coconuts migrate"

#initialize dictionary to store vowel counts
vowel_counts = {'a': 0, 'e': 0, 'i': 0, 'o':0, 'u': 0}

#loop through sentence and update vowel counts as appropriate
for letter in sentence:
    if letter.lower() == 'a':
        vowel_counts['a'] += 1
    elif letter.lower() == 'e':
        vowel_counts['e'] += 1
    elif letter.lower() == 'i':
        vowel_counts['i'] += 1
    elif letter.lower() == 'o':
        vowel_counts['o'] += 1
    elif letter.lower() == 'u':
        vowel_counts['u'] += 1

#display results
print("The sentence has " + str(vowel_counts['a']) + " a's, " + str(vowel_counts['e']) + " e's, " + str(vowel_counts['i']) + " i's, " + str(vowel_counts['o']) + " o's, and " + str(vowel_counts['u']) + " u's.")

#%%
## Q5: Length of All Words in a Sentence
#Create a long sentence of words (assume NO punctuation).
#Put the words into a list (Hint: How are the words separated?). Separating words can be done before the list comprehension.
#Use a list comprehension to return each word along with the length of it. Use: (word, len(word)) in your list comprehension.
#Finally, print out each word and its length (you may use a simple for-loop to do this), but sort by smallest size first (Hint: Search for a method that can sort a list. What do you have to do when you are trying to sort a list of tuples?)

sentence = "This is a very long sentence with lots and lots and lots of words but no punctuation so it is really a very long run on sentence with probably horrible grammar like comma splices and stuff"

#split sentence into words separated by spaces
words = sentence.split(" ")

#get length of each word
word_lens = [(word, len(word)) for word in words]

#sort word-size tuples by length sorted from shortest to longest
word_lens.sort(key = lambda x: x[1])

#print out words and their lenghts
for word in word_lens:
    print("Word: {}, Length: {}".format(word[0], word[1]))


#%%
## Q6: Map/Filter/Reduce Examples
#In the PowerPoint slides describing "higher-order functions" there are three examples: 
#one illustrating the use of map, the next one illustrating the use of filter, and the last one illustrating the use of reduce. 
#Rewrite these three examples without using the map(), filter(), and functools.reduce() functions.

#helper functions from powerpoint:
def square(number):
    return number * number

def sum(x, y):
    return x + y

def even(number):
    if number % 2 == 0:
        return True
    else:
        return False

## MAP
#powerpoint ex with map function:
# numbers = [1,2,3]
# numberssq = list(map(square, numbers))

#rewrite without map function:
numbers = [1,2,3]
numberssq = list()
for num in numbers:
    numberssq.append(square(num))
    
print(numberssq)

## FILTER
#powerpoint ex with filter function:
# numbers = list(range(1,11))
# evens = list(filter(even, numbers))

#rewrite without filter function:
numbers = list(range(1,11))
evens = list()

for num in numbers:
    if even(num):
        evens.append(num)

print(evens)

## REDUCE
#powerpoint ex with functools.reduce function:
# import functools
# numbers = list(range(1,11))
# sum = functools.reduce(sum, numbers)
        
numbers = list(range(1,11))
total = 0

for num in numbers:
    total += num

print("The sum of the range is " + str(total))

#%%
## Q7: Classes and Inheritance
#Create a base class called ACCOUNT.
#Account should have the following attributes: accountNumber and balance, which should be correctly initialized in the constructor (_ _init_ _) method for the class.
#Create a to-string (_ _str_ _) method that prints “Account number 1234” on one line and “Balance: 2000” on the next line (example with account number of 1234 and balance of 2000).
#Create another class called CHECKING. This class should inherit from the Account class. Therefore, the Checking class is the derived class.
#In addition to the accountNumber and balance attributes, the Checking class has a fee attribute (that is used when withdrawing money from the Checking account). Initialize all variables correctly in the constructor (_ _init_ _) method.
#Create a to-string method (_ _str_ _) that is identical to the two-line to-string method of the Account class, but has an additional header (a new first line): "Account type: Checking". Therefore, the to-string method of this class should produce a three-line output.
#Add a method getFee(self) that returns the fee attribute (remember to use: self.fee).
#Add a method deposit(self, amount) that adds the "amount" to the balance. It doesn't produce any output or return anything.
#Add a method withdraw(self, amount) that does the following: (1) checks to see if the amount to withdraw is greater than the balance; if so, display a message "Insufficient funds!", (2) otherwise, adjust the balance so that the amount AND the fee are subtracted. Remember when you make a withdrawal, there is a fee involved that also needs to be subtracted from the balance. (Example: Balance is $500. If you want to withdraw $100, and if the fee is $10, the method checks 100 is not greater than 500, so the resulting balance will be 500 - 100 - 10, so balance = $390.)
#To test this out: (1) create an instance of the Checking class (call it check1) with account number 1234 and a balance of 500 with a fee of 0.50, (2) print check1 out, (2) withdraw $100, (4) print check1 out, (5) deposit $200, (6) print check1 out. See example below.

#create base class
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

#run tests
check1 = Checking("1234", 500, 0.50)
print(check1)

check1.withdraw(100)
print(check1)

check1.deposit(200)
print(check1)

# #other tests
# print(check1.getFee())

# check2 = Checking("1111", 100, 1)
# check2.withdraw(50)
# check1.deposit(50)
# print(check1)
# print(check2)


