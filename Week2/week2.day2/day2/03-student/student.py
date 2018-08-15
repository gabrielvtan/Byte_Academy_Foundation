## Foundation - Week 2 Day 2 Exercise 3 - Student Record
import json
# Create a class representing a record of a student
class Student():
    """ student class for taking grades and returning an average gpa"""

    def __init__(self, first, last, age, grades):

        self.first = first
        self.last = last
        self.age = age
        self.grades = grades

# It should have two methods:
# ```addgrade(grade)``` : appends a grade to the grades list 
    
    def addgrade(self):
        self.grades.append(grade)

# ```gpa()``` returns the student's gpa (the mean value of the grades list)
    def gpa(self):
        average = sum(self.grades)/len(self.grades)
        return round(average)

"""        
def student_list(file):
    with open(file,'r') as jsonfile:
        student_dict = json.load(jsonfile)
        key = ['grades']
        student_gpa = {x:studc}
        return student_dict

print(student_list('student_list.json'))
""""


#### Challenge: 

# Write ```load(filename)``` that takes the name of a file and loads data 
# from it. It is up to you to decide the format of how this data is stored. 
# json might be useful. After load() is called, the member values should all 
# be set to values specified in the file, possibly overwriting existing values.

# Write ```save(filename)``` that saves the data to the format you designed.
