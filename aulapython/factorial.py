def factorial(n):
    result = 1
    while n >= 1:
        result = result * n
        n = n - 1
    return result

print (factorial(4))
print (factorial(0))
print (factorial(10))
print (factorial(20))


