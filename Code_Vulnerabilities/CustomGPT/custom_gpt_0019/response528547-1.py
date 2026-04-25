
# -*- coding: utf-8 -*-
import sys
import ast

# Get the input string from the command line
a = sys.argv[1]

# Safely evaluate the string to interpret escape sequences
evaluated_string = ast.literal_eval(a)

# Encode the evaluated string to bytes
b = evaluated_string.encode('utf-8')

# Print the original string and the byte representation
print(a)
print('\n')
print(b)
