sourcecode file
# String reversal using iterative and recursive methods
# Without using built-in reverse functions

def reverse_iterative(s):
    result = ""
    for i in range(len(s) - 1, -1, -1):
        result += s[i]
    return result


def reverse_recursive(s):
    if len(s) <= 1:
        return s
    return s[-1] + reverse_recursive(s[:-1])


# Test
if __name__ == "__main__":
    original = "Questline"
    print("Original String:", original)
    print("Reversed (Iterative):", reverse_iterative(original))
    print("Reversed (Recursive):", reverse_recursive(original))
