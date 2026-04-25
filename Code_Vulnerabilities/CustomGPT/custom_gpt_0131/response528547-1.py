
# -*- coding: utf-8 -*-
import sys
import ast

# Get the input argument from command line
a = sys.argv[1]

# Convert the string representation of bytes to actual bytes
b = ast.literal_eval(a)  # This evaluates the input string as a Python literal

print(a)   # This will print the original input string
print('\n')
print(b)   # This will print the byte string
