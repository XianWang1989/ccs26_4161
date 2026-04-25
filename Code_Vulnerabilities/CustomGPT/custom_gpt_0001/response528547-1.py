
# -*- coding: utf-8 -*-
import sys

# Get the input string from the command line arguments
a = sys.argv[1]

# Convert the input string representation of bytes into actual bytes
# Using eval to convert the input string to a byte literal
b = eval(a)

# Print the original string and its byte representation
print(a)
print('\n')
print(b)
