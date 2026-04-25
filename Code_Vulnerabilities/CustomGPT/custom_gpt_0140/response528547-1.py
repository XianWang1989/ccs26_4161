
# -*- coding: utf-8 -*-
import sys
import ast

# Get the command line argument
a = sys.argv[1]

# Evaluate the string to convert it to the appropriate byte representation
b = ast.literal_eval(a)

# Print outputs
print(a)
print('\n')
print(b)
