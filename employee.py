__author__ = 'alex.hernandez'

import random


class Employee(object):
    """Models real-life employees!"""
    def __init__(self, employee_name):
        self.employee_name = employee_name

    def getName(self):
        print self.employee_name

    @staticmethod
    def generateId():
        id = random.random()
        print "New ID: " + str(id)
        return id


    def generateEmail(self):
        prefix = self.employee_name.lower()
        email = prefix + "@hernandez.com"
        email = email.replace(" ", "")
        print "Email: " + email
        return email


# Add your code below!
class SoftwareEngineer(Employee):

    @staticmethod
    def calculate_wage():
        total = "Salary: $70,000"
        print total
        return total

    @staticmethod
    def jobTitle():
        title = "Software Engineer"
        print "Job Title: " + title
        return title

# Add your code below!
class Recruiter(Employee):

    @staticmethod
    def calculate_wage():
        total = "Salary: $30,000"
        print total
        return total

    @staticmethod
    def jobTitle():
        title = "Technical Recruiter"
        print "Job Title: " + title
        return title

# Add your code below!
class PlatformTestEngineer(Employee):

    @staticmethod
    def calculate_wage():
        total = "Salary: $61,000"
        print total
        return total

    @staticmethod
    def jobTitle():
        title = "Platform Test Engineer"
        print "Job Title: " + title
        return title

# Add your code below!
class HealthAdministrator(Employee):

    @staticmethod
    def calculate_wage():
        total = "Salary: $50,000"
        print total
        return total

    @staticmethod
    def jobTitle():
        title = "Health Administrator"
        print "Job Title: " + title
        return title


def generateCredentials(fullName, jobTitle):

    if jobTitle == "1":
        employee = SoftwareEngineer(fullName)
        employee.jobTitle()
        employee.calculate_wage()
        employee.generateId()
        employee.generateEmail()

    elif jobTitle == "2":
        employee = Recruiter(fullName)
        employee.jobTitle()
        employee.calculate_wage()
        employee.generateId()
        employee.generateEmail()

    elif jobTitle == "3":
        employee = PlatformTestEngineer(fullName)
        employee.jobTitle()
        employee.calculate_wage()
        employee.generateId()
        employee.generateEmail()

    elif jobTitle == "4":
        employee = HealthAdministrator(fullName)
        employee.jobTitle()
        employee.calculate_wage()
        employee.generateId()
        employee.generateEmail()

