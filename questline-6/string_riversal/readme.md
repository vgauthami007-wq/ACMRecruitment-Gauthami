 String Reversal (Iterative & Recursive)

 Task
Reverse a string using both **iterative** and **recursive** methods without using built-in functions like `[::-1]` or `reversal

 Iterative Method
- Loop through the string from the end to the beginning.
- Append each character to a new string.
- Return the new reversed string.

Pseudo-code:
function reverse_iterative(s):
result = ""
for i from length(s)-1 down to 0:
result = result + s[i]
return result
Recursive Method
- Base case: if the string is empty or has one character, return it.
- Recursive step: return last character + recursive call on substring (excluding last character).

Pseudo-code:
function reverse_recursive(s):
if length(s) <= 1:
return s
return s[-1] + reverse_recursive(s[0 : length(s)-1])
