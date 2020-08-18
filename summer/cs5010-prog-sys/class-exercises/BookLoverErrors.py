#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module 5 Live Session Exercise: Testing Activity
Part 3: intentionally insert errors for someone else's tests to find

Shannon Paylor
sep4hy

Group members: Alex Stern (acs4wq), Congxin Xu (cx2rx), and Taylor Rohrich (trr2as)
"""

class BookLover:
    def __init__(self, name, email, favGenre, numBooks = 0, bookLst = []):
        self.name = name
        self.email = email
        self.favGenre = favGenre
        self.numBooks = numBooks
        self.bookLst = bookLst

    def __str__(self):
        ret_str = self.name + " has read " + str(len(self.bookLst)) + " books:\n"
        ret_str += str(self.bookLst)
        return ret_str

    def addBook(self, bookName, rating):
        self.bookLst.append(bookName)
        
    def hasRead(self, bookName):
        return bookName in self.bookLst
        
    def numBooksRead(self):
        return self.numBooks
        
    def favBooks(self):
        return list(filter(lambda x: x[1] > 4, self.bookLst))


