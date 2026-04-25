
# -*- coding: utf-8 -*-
import sys
import ast

# Get the input from the command line
a = sys.argv[1]

# Convert the input string to bytes
try:
    b = ast.literal_eval(a)
except (SyntaxError, ValueError) as e:
    print(f"Error: {e}")
    exit(1)

# Print the original string and its byte representation
print(a)
print('\n')
print(b)
