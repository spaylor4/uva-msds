# File: AStudent_Class.py
# CS 5010
# Learning Python (Python version: 3)
# Topics:
#     - Used for demonstrating Unit Testing (see AStudent_Class_numCourses_test.py)

class AStudent:
    # fields: name, sid, grades(a list), numCourses
    
    # Local variables
    # grades = []   # to hold grades 
    # courses = []  # to hold enrolled course names e.g. CS5010
    
    def __init__(self, name, sid, numCourses, grades=None, courses=None):  # constructor
        self.name = name    # Student name	
        self.id = sid	      # Student id 
        self.numCourses = numCourses  # The number of courses a student is enrolled in
        if grades is None:  # If no grades parameter was provided
            grades = []     # Empty list, until values added
        #else:
        self.grades = grades  # However, if grades is provided, handle it here
        if courses is None:     # If no courses parameter was provided
            courses = []        # Empty list, until values added
        #else:
        self.courses = courses # However, if courses is provided, handle it here
    
    def enrollInCourse(self, cname): # Enroll in a course
        courseName = cname
        self.courses.append(courseName)
        self.numCourses += 1 # increment the number of courses
            
    def addGrade(self, grade): # add the grade to the list of grades
        self.grades.append(grade)
    
    def showGrades(self): # displaying the grades
        grds = '' # empty string
        for grade in self.grades: # Loop through grades list
            grds += str(grade) + ' '  # assign each grade to the string grds
        return grds
    
    def __str__(self):
        return "Name: " + self.name + "\n" + \
        "Id: " + self.id + "\n" + \
        "Grades: " + self.showGrades() + "\n" + \
        "Courses: " + str(self.courses)
        
    def average(self): # compute the average grade
        total = 0
        for grade in self.grades:
            total += grade
        return total / len(self.grades)
        
# Testing / Usage
#s1 = AStudent("Nada", "711", 0)
#s1.enrollInCourse("CS9999")
#s1.addGrade(99)
#print(s1)