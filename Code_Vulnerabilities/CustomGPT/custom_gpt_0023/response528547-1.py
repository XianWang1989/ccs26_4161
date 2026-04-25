
# -*- coding: utf-8 -*-
import sys
import ast

# Get the input string
a = sys.argv[1]

# Convert string representation of bytes to actual bytes
b = ast.literal_eval(a)

print(a)
print('\n')
print(b)
