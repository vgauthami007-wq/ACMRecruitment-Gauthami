# Iterative Method
def reverse_iterative(text):
    reversed_text = ""      
    for i in range(len(text) - 1, -1, -1):
        reversed_text += text[i]
    return reversed_text


# Recursive Method
def reverse_recursive(text):
    if len(text) <= 1:
        return text
    return text[-1] + reverse_recursive(text[:-1])

if __name__ == "__main__":
    word = "Questline"   # you can change this to test with any word
    print("Original String:", word)
    print("Reversed (Iterative):", reverse_iterative(word))
    print("Reversed (Recursive):", reverse_recursive(word))
