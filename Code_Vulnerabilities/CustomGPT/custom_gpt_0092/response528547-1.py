
# -*- coding: utf-8 -*-
import sys
import ast

# Get the input from command line
a = sys.argv[1]

# Evaluate the input string to get the actual bytes object
b = ast.literal_eval(a)

print(a)
print('\n')
print(b)
