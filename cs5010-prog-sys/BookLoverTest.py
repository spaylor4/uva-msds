#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module 5 Live Session Exercise: Testing Activity
Part 2: write unit tests for BookLover methods

Shannon Paylor
sep4hy

Group members: Alex Stern (acs4wq), Congxin Xu (cx2rx), and Taylor Rohrich (trr2as)
"""

import unittest
# from BookLover import BookLover #test my normal code
# from BookLoverErrors import BookLover #test my buggy code
from bookloverErrorAlex import BookLover #test Alex's code

class BookLoverTestCase(unittest.TestCase):
    def test_add_book_book_list(self):
        #if no book list supplied on creation, does add book method work correctly
        book_lover1 = BookLover("Shelby", "some email", "Biography/Memoir")
        book_lover1.addBook("Grant", 4)
        book_lover1.addBook("Becoming", 4)
        book_lover1.addBook("Bossypants", 3)
        
        self.assertEqual(book_lover1.bookLst, [("Grant", 4), ("Becoming", 4), ("Bossypants", 3)])

    def test_add_book_num_books(self):
        
        book_lover1 = BookLover("Shelby", "some email", "Biography/Memoir", 
                                numBooks = 1, bookLst = [("Pillars of the Earth", 1)])
        book_lover2 = BookLover("Ben", "another email", "Sci-Fi")
        book_lover1.addBook("Grant", 4)
        book_lover1.addBook("Becoming", 4)
        book_lover1.addBook("Bossypants", 3)
        book_lover2.addBook("Ender's Game", 3)
        
        self.assertEqual(book_lover1.numBooks, 4)
        
    def test_has_read_true(self):
        book_lover1 = BookLover("Shelby", "some email", "Biography/Memoir")
        book_lover1.addBook("Grant", 4)
        self.assertTrue(book_lover1.hasRead("Grant"))
        
    def test_has_read_false(self):
        book_lover1 = BookLover("Shelby", "some email", "Biography/Memoir")
        book_lover1.addBook("Grant", 4)
        self.assertFalse(book_lover1.hasRead("Ender's Game"))
        
    def test_num_books_no_books(self):
        book_lover1 = BookLover("Shelby", "some email", "Biography/Memoir")
        
        self.assertEqual(book_lover1.numBooksRead(), 0)
        
    def test_num_books_many_books(self):
        book_lover1 = BookLover("Shelby", "some email", "Biography/Memoir", 
                                numBooks = 1, bookLst = [("Pillars of the Earth", 1)])
        book_lover1.addBook("Grant", 4)
        book_lover1.addBook("Becoming", 4)
        book_lover1.addBook("Bossypants", 3)
        
        self.assertEqual(book_lover1.numBooksRead(), 4)
        
    def test_fav_books_no_favs(self):
        book_lover1 = BookLover("Shelby", "some email", "Biography/Memoir", 
                                numBooks = 1, bookLst = [("Pillars of the Earth", 1)])
        
        self.assertEqual(book_lover1.favBooks(), [])
        
    def test_fav_books(self):
        book_lover1 = BookLover("Shelby", "some email", "Biography/Memoir", 
                                numBooks = 1, bookLst = [("Pillars of the Earth", 1)])
        book_lover1.addBook("Grant", 4)
        book_lover1.addBook("Becoming", 4)
        book_lover1.addBook("Bossypants", 3)
        
        self.assertEqual(book_lover1.favBooks(), [("Grant", 4), ("Becoming", 4)])


if __name__ == '__main__':
    unittest.main()