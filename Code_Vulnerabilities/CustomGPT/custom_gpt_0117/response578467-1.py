
# Define the custom alphabet
alphabet = "abcdefghijklmnopqrstuvwxyz0123456789 .,?!"

def custom_ord(char):
    # Check if the char is in the alphabet
    if char in alphabet:
        return alphabet.index(char)
    else:
        raise ValueError(f"Character '{char}' is not in the defined alphabet.")

# Example usage
print(custom_ord("a"))  # Output: 0
print(custom_ord("b"))  # Output: 1
print(custom_ord("c"))  # Output: 2
