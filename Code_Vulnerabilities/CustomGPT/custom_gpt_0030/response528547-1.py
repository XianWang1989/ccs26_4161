
# -*- coding: utf-8 -*-
import sys
import ast

# Get the input argument
a = sys.argv[1]

# Use ast.literal_eval to safely evaluate the string to a bytes object
b = ast.literal_eval(a)

# Print the original string and its bytes representation
print(a)
print('\n')
print(b)
