
# -*- coding: utf-8 -*-
import sys
import ast

# Get the input from command line
a = sys.argv[1]

# Use ast.literal_eval to safely evaluate the input string
decoded_string = ast.literal_eval(a)
b = decoded_string.encode('utf-8')

# Print the original input and the byte representation
print(a)
print('\n')
print(b)
