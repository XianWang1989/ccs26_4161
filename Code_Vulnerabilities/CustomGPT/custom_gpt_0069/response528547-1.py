
# -*- coding: utf-8 -*-
import sys
import ast

# Get input from command line
a = sys.argv[1]

# Convert the input string representation of bytes to actual bytes
b = ast.literal_eval(a)

print(a)  # Print original input
print('\n')
print(b)  # Print bytes
