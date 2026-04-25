
# -*- coding: utf-8 -*-
import sys
import ast

# Get the input string from the command line
a = sys.argv[1]

# Use ast.literal_eval to safely evaluate the string representation of bytes
b = ast.literal_eval(a)

# Print the original string and the byte representation
print(a)
print('\n')
print(b)
