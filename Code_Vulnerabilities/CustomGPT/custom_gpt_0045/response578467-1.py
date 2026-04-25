
# Define the custom alphabet
alphabet = "abcdefghijklmnopqrstuvwxyz0123456789 .,?!"

def custom_ord(char):
    # Find the index of the character in the custom alphabet
    index = alphabet.find(char)
    # Return the index or raise an error if the character is not found
    if index != -1:
        return index
    else:
        raise ValueError(f"Character '{char}' not found in the custom alphabet.")

# Example usage
print(custom_ord("a"))  # Output: 0
print(custom_ord("b"))  # Output: 1
print(custom_ord("c"))  # Output: 2
print(custom_ord("1"))  # Output: 26 (for example, if '1' is at position 26 in alphabet)
