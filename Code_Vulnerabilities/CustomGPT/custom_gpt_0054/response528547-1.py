
# -*- coding: utf-8 -*-
import sys
import ast

# Take the input from the command line
a = sys.argv[1]

# Use ast.literal_eval to safely evaluate the string as a bytes literal
b = ast.literal_eval(a)

print(a)
print('\n')
print(b)
