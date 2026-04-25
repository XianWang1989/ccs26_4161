
# -*- coding: utf-8 -*-
import sys
import ast

# Get the input from command line
a = sys.argv[1]

# Convert the escaped string to bytes
b = bytes(ast.literal_eval(a))

print(a)  # Original string
print('\n')
print(b)  # Output as bytes
