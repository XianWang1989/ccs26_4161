
# -*- coding: utf-8 -*-
import sys
import ast

# Read the input from command line
a = sys.argv[1]

# Safely evaluate the input string to get the bytes representation
b = ast.literal_eval(a)

# Print the original string and the byte representation
print(a)
print('\n')
print(b)
