__author__ = 'alex.hernandez'

import sys
import os
import employee


# Create the restart function to restart the program

def restart_program():

    python = sys.executable
    os.execl(python, python, *sys.argv)

print "\n\n\nPRESS CTRL + C AT ANYTIME TO CLOSE THE PROGRAM"

print "\n"

# Store the Full Name

fullName = raw_input("What is the New Hire's full name: ")

# Store the Job Title

jobTitle = raw_input("What is his/hers job title: \n 1 = Software Engineer \n 2 = Technical Recruiter "
                   "\n 3 = Platform Test Engineer \n 4 = Health Administrator \n > ")

# Store the Job Title

currentEmail = raw_input("What is your current Email: ")

currentNumber = raw_input("What is your current Phone #: ")

print "\n"

# Generate the Employee Credentials

employee.generateCredentials(fullName, jobTitle, currentEmail, currentNumber)

# Call the restart function

restart_program()