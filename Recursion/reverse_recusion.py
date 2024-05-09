def reverse_str(str1):
    if len(str1) == 1:
        return str1
    return reverse_str(str1[1:]) + str1[0]

print(reverse_str("anwar musthafa"))