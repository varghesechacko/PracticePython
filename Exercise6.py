# Ask the user for a string and print out whether this string is a palindrome or not.

userString = input ("Enter a string: ")

reversedString = userString[::-1]

if userString == reversedString: print ("Your string is a palindrome")
else: print ("Your string is not a palindrome")

# a = [1,2,3,4,5,6,7,8,9,10]

# print (a[5::-3])