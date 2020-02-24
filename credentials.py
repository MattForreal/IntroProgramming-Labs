# CMPT 120 Intro to Programming
# Lab #5 – Working with Strings and Functions
# Author: Matt Farrell
# Created: 2020-02-24

def name():
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    return first, last

def username():
    # get user's first and last names
    # TODO modify this to generate a Marist-style username
    first, last = name()
    uname = first + "." + last
    print("Here is your Marist-style username.", uname.lower())
    print("Your Marist-style email will be:", uname.lower(),"@marist.edu")

def pwstrength():
    passwd = input("Create a new password: ")
    # TODO modify this to ensure the password has at least 8 characters
    if len(passwd) < 8:
        print("My bad dawg, needs to be at least 8 characters.")
        passwd = input("Create a new password: ")
    if (passwd.isupper() or passwd.islower()):
        print("Password would be much stronger with upper and lower case don't you think?")
        passwd = input("Create a new password: ")
    print("Here is your new password.", passwd)

def password():
    # ask user to create a new password
    username()
    pwstrength()

password()
