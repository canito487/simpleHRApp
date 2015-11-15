import sys
import os
import employee

__author__ = 'alex.hernandez'


# Create the restart function to restart the program

def restart_program():

    python = sys.executable
    os.execl(python, python, *sys.argv)

print "\nPRESS CTRL + C AT ANYTIME TO CLOSE THE PROGRAM"

print "\n"

# Store the Full Name

fullName = raw_input("What is the New Hire's full name: ")

# Store the Job Title

jobTitle = raw_input("What is his/hers job title: \n 1 = Software Engineer \n 2 = Technical Recruiter "
                   "\n 3 = Platform Test Engineer \n 4 = Health Administrator \n > ")

# Store the employee's email

currentEmail = raw_input("What is your current Email: ")

# Store the employee's current Phone #

currentNumber = raw_input("What is your current Phone #: ")

print "\n"

# Generate the Employee Credentials

employee.generateCredentials(fullName, jobTitle, currentEmail, currentNumber)

# Call the restart function

restart_program()
