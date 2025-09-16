# Questline-3: Euler Start

# Problem 1
# Multiples of 3 or 5

for i in range(1000):
    if i%3==0 or i%5==0:
      total+=i
print(total)

# Problem 2
# Even Fibonacci Number

a, b = 1, 2   # first two Fibonacci numbers
total = 0

while b <= 4000000:
    if b % 2 == 0:          
        total += b           
    a, b = b, a + b          

print(total)   # 4613732
