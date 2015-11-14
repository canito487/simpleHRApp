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
        title = "Job Title: " + title
        print title
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
        title = "Job Title: " + title
        print title
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
        title = "Job Title: " + title
        print title
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
        title = "Job Title: " + title
        print title
        return title


def generateCredentials(fullName, jobTitle, currentEmail):

    subjectText = fullName + "'s " + "Credentials"

    emailText = []

    if jobTitle == "1":
        employee = SoftwareEngineer(fullName)
        emailText.append(employee.jobTitle())
        emailText.append(employee.calculate_wage())
        emailText.append(employee.generateId())
        emailText.append(employee.generateEmail())

    elif jobTitle == "2":
        employee = Recruiter(fullName)
        emailText.append(employee.jobTitle())
        emailText.append(employee.calculate_wage())
        emailText.append(employee.generateId())
        emailText.append(employee.generateEmail())

    elif jobTitle == "3":
        employee = PlatformTestEngineer(fullName)
        emailText.append(employee.jobTitle())
        emailText.append(employee.calculate_wage())
        emailText.append(employee.generateId())
        emailText.append(employee.generateEmail())

    elif jobTitle == "4":
        employee = HealthAdministrator(fullName)
        emailText.append(employee.jobTitle())
        emailText.append(employee.calculate_wage())
        emailText.append(employee.generateId())
        emailText.append(employee.generateEmail())

    send_email(currentEmail, subjectText, emailText)

def send_email(currentEmail, subject, body):
    import smtplib

    gmail_user = ""
    gmail_pwd = ""
    FROM = ""
    TO = currentEmail if type(currentEmail) is list else [currentEmail]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        # SMTP_SSL Example
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print "\n"
        print 'successfully sent the mail'
    except:
        print "failed to send mail"

