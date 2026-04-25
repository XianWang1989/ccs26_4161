
# -*- coding: utf-8 -*-
import sys
import ast

# Get the input from command line
a = sys.argv[1]

# Convert the string representation of bytes to an actual bytes object
b = ast.literal_eval(a)

# Print the original string
print(a)
print('\n')

# Print the bytes representation
print(b)
