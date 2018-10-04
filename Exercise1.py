# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

# Extras:

# Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
# Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)

from datetime import date

name = input("What is your name: ")
age = input("Enter your age: ")

yearsTo100 = 100 - int(age)
currentYear = date.today().year

def printCopies():
    print(name + ", you will hundred in " + str(currentYear + yearsTo100))

numberOfCopies = input("Enter a number: ")

for i in range(0, int(numberOfCopies)):
    printCopies()

