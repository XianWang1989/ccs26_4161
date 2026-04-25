
# -*- coding: utf-8 -*-
import sys
import ast

a = sys.argv[1]

# Use ast.literal_eval to evaluate the literal as Python expression
b = ast.literal_eval(a)

# Print the original string and its bytes representation
print(a)
print('\n')
print(b)
