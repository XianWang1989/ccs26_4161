
alphabet = "abcdefghijklmnopqrstuvwxyz0123456789 .,?!"

def custom_ord(char):
    if char in alphabet:
        return alphabet.index(char)
    else:
        # You can return -1 or any other value to indicate the character isn't found
        return -1

# Test the custom function
print(custom_ord("a"))  # Output: 0
print(custom_ord("b"))  # Output: 1
print(custom_ord("c"))  # Output: 2
print(custom_ord("1"))  # Output: 26 (as '1' is the 27th character in the string)
print(custom_ord("!"))  # Output: 36 (as '!' is the 37th character)
