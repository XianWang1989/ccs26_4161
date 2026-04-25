
# Define the custom alphabet
alphabet = "abcdefghijklmnopqrstuvwxyz0123456789 .,?!"

# Function to get the custom ordinal value
def custom_ord(char):
    # Find the index of the character in the alphabet
    index = alphabet.find(char)
    # If the character is not found, you could return None or raise an error
    if index == -1:
        raise ValueError(f"Character '{char}' not found in custom alphabet.")
    return index

# Example usage
print(custom_ord("a"))  # Output: 0
print(custom_ord("b"))  # Output: 1
print(custom_ord("c"))  # Output: 2
print(custom_ord("9"))  # Output: 36
