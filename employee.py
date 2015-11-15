__author__ = 'alex.hernandez'

import random


# Create a Base Employee Object
class Employee(object):
    """Models real-life employees!"""
    def __init__(self, employee_name):
        self.employee_name = employee_name

    def getName(self):
        print self.employee_name

    @staticmethod
    def generateId():
        id = random.random()
        id = "New ID: " + str(id)
        print "New ID: " + str(id)
        return id

    def generateEmail(self):
        prefix = self.employee_name.lower()
        email = prefix + "@hernandez.com"
        email = email.replace(" ", "")
        email = "Email: " + email
        print email
        return email


# Software Engineer Object
class SoftwareEngineer(Employee):

    @staticmethod
    def calculate_wage():
        total = "Salary: $70,000"
        print total
        return total

    @staticmethod
    def jobTitle():
        title = "Software Engineer"
        title = "Job Title: " + title
        print title
        return title

# Recruiter Object
class Recruiter(Employee):

    @staticmethod
    def calculate_wage():
        total = "Salary: $30,000"
        print total
        return total

    @staticmethod
    def jobTitle():
        title = "Technical Recruiter"
        title = "Job Title: " + title
        print title
        return title

# PlatformTestEngineer Object
class PlatformTestEngineer(Employee):

    @staticmethod
    def calculate_wage():
        total = "Salary: $61,000"
        print total
        return total

    @staticmethod
    def jobTitle():
        title = "Platform Test Engineer"
        title = "Job Title: " + title
        print title
        return title

# Health Administrator Object
class HealthAdministrator(Employee):

    @staticmethod
    def calculate_wage():
        total = "Salary: $50,000"
        print total
        return total

    @staticmethod
    def jobTitle():
        title = "Health Administrator"
        title = "Job Title: " + title
        print title
        return title

# This function generates the credentials of the new employee
def generateCredentials(fullName, jobTitle, currentEmail, currentNumber):

    subjectText = fullName + "'s " + "Credentials"

    emailText = []

    # This function compiles the credentials of the employee after new object has been instantiated
    def compileCredentials(employee):
        emailText.append(employee.jobTitle())
        emailText.append(employee.calculate_wage())
        emailText.append(employee.generateId())
        emailText.append(employee.generateEmail())

    if jobTitle == "1":
        employee = SoftwareEngineer(fullName)
        compileCredentials(employee)

    elif jobTitle == "2":
        employee = Recruiter(fullName)
        compileCredentials(employee)

    elif jobTitle == "3":
        employee = PlatformTestEngineer(fullName)
        compileCredentials(employee)

    elif jobTitle == "4":
        employee = HealthAdministrator(fullName)
        compileCredentials(employee)

    send_email(currentEmail, currentNumber, subjectText, emailText)

# This function sends a confirmation email and text
def send_email(currentEmail, currentNumber, subject, body):
    import smtplib

    gmail_user = ""
    gmail_pwd = ""
    FROM = ""
    TOEMAIL = currentEmail if type(currentEmail) is list else [currentEmail]
    TONUMBER = currentNumber + "@txt.att.net"
    SUBJECT = subject
    TEXT = body

    # Prepare to send email message
    message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TOEMAIL), SUBJECT, TEXT)
    try:

        server_ssl = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server_ssl.ehlo() # optional, called by login()
        server_ssl.login(gmail_user, gmail_pwd)
        server_ssl.sendmail(FROM, TOEMAIL, message)
        server_ssl.close()
        print "\n"
        print 'Succesfully sent the Email confirmation'
    except:
        print "failed to send mail"

    # Prepare to send txt message
    # Use sms gateway provided by mobile carrier:
    # at&t:     number@txt.att.net
    # t-mobile: number@tmomail.net
    # verizon:  number@vtext.com
    # sprint:   number@page.nextel.com
    message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TONUMBER), SUBJECT, TEXT)
    try:

        server_ssl = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server_ssl.ehlo() # optional, called by login()
        server_ssl.login(gmail_user, gmail_pwd)
        server_ssl.sendmail(FROM, TONUMBER, message)
        server_ssl.close()
        print "\n"
        print 'Successfully sent the TXT'
    except:
        print "Failed to send TXT"

