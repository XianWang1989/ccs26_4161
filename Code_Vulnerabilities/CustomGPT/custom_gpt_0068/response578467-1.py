
# Define the custom alphabet
alphabet = "abcdefghijklmnopqrstuvwxyz0123456789 .,?!"

def custom_ord(char):
    # Check if the character is in the custom alphabet
    if char in alphabet:
        # Return the index of the character in the alphabet
        return alphabet.index(char)
    else:
        # Optionally handle characters not in the alphabet
        return None  # or raise an exception, or return -1, etc.

# Example usage
print(custom_ord("a"))  # Output: 0
print(custom_ord("b"))  # Output: 1
print(custom_ord("c"))  # Output: 2
print(custom_ord("z"))  # Output: 25
print(custom_ord("1"))  # Output: 26
print(custom_ord(" "))  # Output: 32
print(custom_ord("?"))  # Output: 35
