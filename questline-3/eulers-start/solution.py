# Questline-3: Euler Start

# Problem 1
# Multiples of 3 or 5

def problem1(limit=1000):
    """Return the sum of all multiples of 3 or 5 below limit."""
    return sum(i for i in range(limit) if i % 3 == 0 or i % 5 == 0)

# Problem 2
# Even Fibonacci Number
def problem2(limit=4000000):
    """Return the sum of even Fibonacci numbers below limit."""
    a, b = 1, 2
    total = 0
    while b < limit:
        if b % 2 == 0:
            total += b
        a, b = b, a + b
    return total
  
if __name__ == "__main__":
    print("Problem 1 Answer:", problem1())
    print("Problem 2 Answer:", problem2())
