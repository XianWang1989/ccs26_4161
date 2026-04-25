
# -*- coding: utf-8 -*-
import sys
import ast

# Get the input from command line
a = sys.argv[1]

# Convert the input string to bytes using ast.literal_eval
b = ast.literal_eval(a)

# Print the original string and the byte representation
print(a)
print('\n')
print(b)
