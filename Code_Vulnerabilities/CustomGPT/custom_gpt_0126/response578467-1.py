
alphabet = "abcdefghijklmnopqrstuvwxyz0123456789 .,?!"

def custom_ord(char):
    index = alphabet.find(char)
    if index == -1:
        raise ValueError(f"Character '{char}' is not in the alphabet.")
    return index

# Example usage
print(custom_ord("a"))  # Output: 0
print(custom_ord("b"))  # Output: 1
print(custom_ord("c"))  # Output: 2
