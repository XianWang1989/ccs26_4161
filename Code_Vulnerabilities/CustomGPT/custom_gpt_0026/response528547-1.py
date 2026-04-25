
# -*- coding: utf-8 -*-
import sys
import ast

# Get the input from command line
a = sys.argv[1]

# Convert the input string to a bytes object
b = ast.literal_eval(a)

# Print the original and byte-encoded values
print(a)
print('\n')
print(b)
