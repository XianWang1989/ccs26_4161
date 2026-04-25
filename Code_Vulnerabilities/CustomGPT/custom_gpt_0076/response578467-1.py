
# Define the custom alphabet
alphabet = "abcdefghijklmnopqrstuvwxyz0123456789 .,?!"

def custom_ord(char):
    # Get the index of the character in the alphabet string
    index = alphabet.find(char)
    if index == -1:
        raise ValueError(f"Character '{char}' not found in the custom alphabet.")
    return index

# Example usage
print(custom_ord("a")) # Returns 0
print(custom_ord("b")) # Returns 1
print(custom_ord("c")) # Returns 2
print(custom_ord("0")) # Returns 26
print(custom_ord(" ")) # Returns 36
