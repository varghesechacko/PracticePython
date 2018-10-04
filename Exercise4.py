# Divisors

userNumber = input ("Enter a number: ")
listOfDivisors = []
userNumber = int (userNumber)

for i in range (1,userNumber + 1):
    if (userNumber % i == 0):
        listOfDivisors.append (i)

print (listOfDivisors)