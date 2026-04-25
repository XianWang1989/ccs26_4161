
# -*- coding: utf-8 -*-
import sys
import ast

# Get the encrypted input from command line
a = sys.argv[1]

# Evaluate the input string to its byte representation
b = ast.literal_eval(a)

# Print the original string and the byte representation
print(a)
print('\n')
print(b)
