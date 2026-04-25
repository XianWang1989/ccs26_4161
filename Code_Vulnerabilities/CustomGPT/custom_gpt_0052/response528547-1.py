
# -*- coding: utf-8 -*-
import sys
import ast

# Get the input from the command line
a = sys.argv[1]

# Safely evaluate the input to convert the string representation of bytes to actual bytes
b = ast.literal_eval(a)

print(a)
print('\n')
print(b)
