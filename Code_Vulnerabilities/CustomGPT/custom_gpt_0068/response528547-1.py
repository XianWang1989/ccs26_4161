
# -*- coding: utf-8 -*-
import sys
import ast

# Input is passed from the command line
a = sys.argv[1]

# Convert the input string representation to actual bytes
b = ast.literal_eval(a)

# Output the original string and the byte output
print(a)
print('\n')
print(b)
