#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module 5 Exercise: Python Unit Testing
Shannon Paylor
sep4hy
"""

import unittest
from AStudent_Class import AStudent

class StudentTestCase(unittest.TestCase):
    def test_add_grade(self):
        #add grade method should take a given grade and append it to the student's list of grades
        #instantiate student and perform operations
        test_student = AStudent("Test Student", "1234", 2, courses = ["Stats", "CompSci"])
        test_student.addGrade(90)
        test_student.addGrade(85)
        test_student.addGrade(87)
        
        #assert expected vs actual
        self.assertEqual(test_student.grades, [90, 85, 87])
        
    def test_average_grade(self):
        #average method should return the average of all of the student's grades
        #instantiate student and perform operations
        test_student = AStudent("Test Student", "1234", 2, courses = ["Stats", "CompSci"])
        test_student.addGrade(90)
        test_student.addGrade(85)
        test_student.addGrade(87)
        
        test_student_avg = test_student.average()
        
        #assert expected vs actual
        expected_val = (90 + 85 + 87) / 3
        self.assertEqual(test_student_avg, expected_val)
        
        

if __name__ == '__main__':
    unittest.main()
