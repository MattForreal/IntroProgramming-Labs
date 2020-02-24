# CMPT 120 Intro to Programming
# Lab #5 – Working with Strings and Functions
# Author: Matt Farrell
# Created: 2020-02-24

def name():
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    dog = first, last
    return first, last

def username():
    # get user's first and last names
    # TODO modify this to generate a Marist-style username
    first, last = name()
    uname = first + "." + last
    print("Here is your Marist-style username.", uname)

def password():
    # ask user to create a new password
    username()
    passwd = input("Create a new password: ")
    # TODO modify this to ensure the password has at least 8 characters
    if len(passwd) < 8:
        print("My bad dawg, needs to be at least 8 characters.")
        passwd = input("Create a new password: ")
    print("Here is your new password.", passwd)
    
password()
