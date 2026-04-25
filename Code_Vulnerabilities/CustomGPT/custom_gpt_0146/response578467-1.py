
# Define the alphabet string
alphabet = "abcdefghijklmnopqrstuvwxyz0123456789 .,?!"

# Function to get the custom ordinal value
def custom_ord(char):
    if char in alphabet:
        return alphabet.index(char)  # Get the index of the character
    else:
        return None  # Return None if the character is not in the alphabet

# Example usage
print(custom_ord("a"))  # Output: 0
print(custom_ord("b"))  # Output: 1
print(custom_ord("c"))  # Output: 2
print(custom_ord("z"))  # Output: 25
print(custom_ord("0"))  # Output: 26
print(custom_ord(" "))  # Output: 36
