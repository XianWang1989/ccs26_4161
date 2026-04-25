
# -*- coding: utf-8 -*-
import sys
import ast

# Get the input from the command line
a = sys.argv[1]

# Safely evaluate the input string to get the byte representation
b = ast.literal_eval(a)

# Print the original string and its byte representation
print(a)
print('\n')
print(b)
