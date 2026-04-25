
alphabet = "abcdefghijklmnopqrstuvwxyz0123456789 .,?!"

# Creating a mapping dictionary
custom_ord = {char: index for index, char in enumerate(alphabet)}

# Testing the custom ord function
print(custom_ord["a"])  # Output: 0
print(custom_ord["b"])  # Output: 1
print(custom_ord["c"])  # Output: 2
print(custom_ord["1"])  # Output: 26
print(custom_ord[" "])  # Output: 36
