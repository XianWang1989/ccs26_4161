
# -*- coding: utf-8 -*-
import sys
import ast

# Get the input from command line
a = sys.argv[1]

# Convert the string representation of bytes to actual bytes
b = ast.literal_eval(a)

# Print the original input and the bytes
print(a)
print('\n')
print(b)
