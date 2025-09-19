# Iterative method
def iterative(s):
    r = ""
    for i in s:
        r =i+r 
    return r


# Recursive method
def recursive(s):
    return s[::-1] 


s = "unibic"
print("Original string:", s)
print("Reversed (Iterative):", iterative(s))
print("Reversed (Recursive):", recursive(s))

