
alphabet = "abcdefghijklmnopqrstuvwxyz0123456789 .,?!"

def custom_ord(char):
    # Find the index of the character in the alphabet string
    index = alphabet.find(char)
    # Return the index, or None if the character is not found
    return index if index != -1 else None

# Example usage
print(custom_ord("a"))  # Output: 0
print(custom_ord("b"))  # Output: 1
print(custom_ord("c"))  # Output: 2
