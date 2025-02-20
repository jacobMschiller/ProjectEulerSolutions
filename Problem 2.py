import math

def fibonacci(n): # Returns nth Fibonacci number
    return math.floor(1/math.sqrt(5) * ((1 + math.sqrt(5))/2)**n - 1/math.sqrt(5) * ((1 - math.sqrt(5))/2)**n)

total = 0
term = 0
i = 3
while True:
    term = fibonacci(i)
    if term > 4000000:
        break
    else:
        if term % 2 == 0:
            total += term
        i += 1
print(total)
