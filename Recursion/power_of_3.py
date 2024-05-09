def power_of_3(n):
    if n == 0:
        return 1
    else:
        return 3 * power_of_3(n - 1)

result = power_of_3(4)
print(result)
