# Binary Palindrome Checker

# ask user for two numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# function to check palindrome
def is_palindrome(n):
    binary = bin(n)[2:]   # get binary without '0b'
    if binary == binary[::-1]:
        print(n, "in binary", binary, "is a PALINDROME")
    else:
        print(n, "in binary", binary, "is NOT a palindrome")

# check both numbers
is_palindrome(num1)
is_palindrome(num2)

