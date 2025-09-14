num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

def check_binary_palindrome(n):
    b = bin(n)[2:]  # convert to binary
    if b == b[::-1]:
        print(f"{n} in binary {b} is a palindrome")
    else:
        print(f"{n} in binary {b} is NOT a palindrome")

check_binary_palindrome(num1)
check_binary_palindrome(num2)
