
# -*- coding: utf-8 -*-
import sys
import ast

# Get the input from command line
a = sys.argv[1]

# Use ast.literal_eval to safely evaluate the string representation of bytes
b = ast.literal_eval(a)

print(a)
print('\n')
print(b)
