def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Example usage:
n = 10
print("Fibonacci series:")
for i in range(n):
    print(fibonacci(i), end=" ")
