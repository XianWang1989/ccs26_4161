
alphabet = "abcdefghijklmnopqrstuvwxyz0123456789 .,?!"

def custom_ord(char):
    index = alphabet.find(char)
    if index != -1:
        return index
    else:
        raise ValueError(f"Character {char} not found in alphabet.")

# Example usage
print(custom_ord("a"))  # Output: 0
print(custom_ord("b"))  # Output: 1
print(custom_ord("c"))  # Output: 2
print(custom_ord("9"))  # Output: 35
print(custom_ord(" "))  # Output: 36
