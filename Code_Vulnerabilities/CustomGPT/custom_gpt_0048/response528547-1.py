
# -*- coding: utf-8 -*-
import sys
import ast

# Read the input from command line
a = sys.argv[1]

# Convert the string representation of bytes to actual bytes
b = ast.literal_eval(a)

# Print the original string and its byte representation
print(a)
print('\n')
print(b)
