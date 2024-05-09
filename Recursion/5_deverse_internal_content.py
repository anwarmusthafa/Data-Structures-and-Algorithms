def reverse_words(s):
    # Split the string into words
    words = s.split()

    # Define a helper function to reverse a word recursively
    def reverse_word(word):
        if len(word) == 0:
            return ""
        else:
            return reverse_word(word[1:]) + word[0]

    # Reverse each word using recursion
    reversed_words = [reverse_word(word) for word in words]

    # Join the reversed words back into a string
    reversed_string = " ".join(reversed_words)
    return reversed_string

# Example usage
s = "My name is Anwar"
print(reverse_words(s))
