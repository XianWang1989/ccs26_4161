
# -*- coding: utf-8 -*-
import sys
import ast

# Take input from command line argument
a = sys.argv[1]

# Convert the input string representation of bytes to an actual bytes object
b = ast.literal_eval(a)

# Print the original string and its byte representation
print(a)
print('\n')
print(b)
