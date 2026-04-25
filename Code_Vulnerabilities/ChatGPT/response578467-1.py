
def custom_ord(char):
    alphabet = "abcdefghijklmnopqrstuvwxyz0123456789 .,?!"

    # Find the index of the character in the alphabet string
    index = alphabet.find(char)

    # If the character is not found, you can return a default value, or raise an error
    if index == -1:
        raise ValueError(f"Character '{char}' not found in the custom alphabet.")

    return index

# Example usage
print(custom_ord("a"))  # Output: 0
print(custom_ord("b"))  # Output: 1
print(custom_ord("c"))  # Output: 2
print(custom_ord("1"))  # Output: 26
print(custom_ord(" "))  # Output: 33
