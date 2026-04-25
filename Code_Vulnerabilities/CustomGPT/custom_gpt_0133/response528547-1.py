
# -*- coding: utf-8 -*-
import sys
import ast

# Get the input from command line
a = sys.argv[1]

# Use ast.literal_eval to interpret the string as a byte array
b = ast.literal_eval(a)

print(a)  # Original input
print('\n')
print(b)  # Actual bytes
