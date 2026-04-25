
def custom_ord(char):
    alphabet = "abcdefghijklmnopqrstuvwxyz0123456789 .,?!"
    index = alphabet.find(char)
    return index if index != -1 else None  # Return None for characters not in alphabet

# Example usage
print(custom_ord("a"))  # Outputs: 0
print(custom_ord("b"))  # Outputs: 1
print(custom_ord("c"))  # Outputs: 2
