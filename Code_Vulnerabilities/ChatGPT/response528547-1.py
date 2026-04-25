
# -*- coding: utf-8 -*-
import sys
import ast

# Take input from command line
a = sys.argv[1]

# Convert the input string to bytes
# Remove the leading 'b' and evaluate the string using ast.literal_eval to interpret escape sequences
b = ast.literal_eval(a)

print(a)       # original input
print('\n')
print(b)       # bytes
