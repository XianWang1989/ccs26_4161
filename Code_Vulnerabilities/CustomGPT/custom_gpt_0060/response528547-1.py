
# -*- coding: utf-8 -*-
import sys
import ast

# Get input from command line
a = sys.argv[1]

# Convert the string representation of bytes into actual bytes
b = ast.literal_eval(a)

# Print the original string and its byte representation
print(a)
print('\n')
print(b)
