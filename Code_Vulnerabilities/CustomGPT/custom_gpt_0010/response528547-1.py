
# -*- coding: utf-8 -*-
import sys

# Get the input string from command line argument
a = sys.argv[1]

# Convert the input string to bytes
b = eval(a)  # Use eval to convert the string representation of bytes into actual bytes

# Print the original string and the bytes
print(a)
print('\n')
print(b)
