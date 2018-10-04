# Odd or Even

number1 = input("Enter a number \n")
number2 = input("Enter another number \n")

number1 = int(number1)
number2 = int(number2)

if (number1 % number2 == 0):
    print(str(number1) + " is divisible by " + str(number2))
else:
    print(str(number1) + " is NOT divisible by " + str(number2))

# if(number % 4 == 0):
#     print("The number you entered is a multiple of 4")
# elif(number % 2 == 0):
#     print("You entered a prime number)")
# else:
#     print("You entered an odd number")
