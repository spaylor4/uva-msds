#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
In-Class Assignment 2: Python
Shannon Paylor
sep4hy
"""

##################
# -- EXERCISE -- #
##################

# Create a long sentence of words [assume NO punctuation]
# Put the words into a list (hint, how are the words separated?)
#        (separating the words can be done before the list comprehension)
# Use a list comprehension to return the word along with the length of it
# Use this -->  (word, len(word))   in your list comprehension
# [finally, print out the words along with its length ] - at the end

sentence = "This is a very long sentence with lots and lots and lots of words but no punctuation so it is really a very long run on sentence with probably horrible grammar like comma splices and stuff"

words = sentence.split(" ")

word_lens = [(word, len(word)) for word in words]

print(word_lens)



