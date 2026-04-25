
# -*- coding: utf-8 -*-
import sys
import ast

# Read input from command line
a = sys.argv[1]

# Use ast.literal_eval to safely interpret the string
interpreted_string = ast.literal_eval(a)

# Encode the interpreted string to bytes
b = interpreted_string.encode('utf-8')

# Print outputs
print(a)
print('\n')
print(b)
