
# Step 1: Define the character mapping string
alphabet = "abcdefghijklmnopqrstuvwxyz0123456789 .,?!"

# Step 2: Define the custom ord function
def custom_ord(char):
    # Step 3: Return the index of the character in the alphabet string
    return alphabet.index(char)

# Step 4: Test the function
print(custom_ord("a"))  # Output: 0
print(custom_ord("b"))  # Output: 1
print(custom_ord("c"))  # Output: 2
print(custom_ord("1"))  # Output: 26
print(custom_ord(" "))  # Output: 36 (assuming space is included)
