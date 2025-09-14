# Find 8-bit 2's complement of -42

num = -42
bits = 8

# formula: (2^bits + num) gives the 2's complement value
value = (1 << bits) + num

# convert to binary
binary = format(value, '08b')

print("Decimal:", num)
print("2's complement (8-bit):", binary)

output
Decimal: -42
2's complement (8-bit): 11010110
