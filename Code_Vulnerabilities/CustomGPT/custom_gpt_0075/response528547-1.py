
# -*- coding: utf-8 -*-
import sys
import ast

# Take input from command line
a = sys.argv[1]

# Evaluate string representation to convert to bytes
b = ast.literal_eval(a)

# Print the original string and its byte representation
print(a)
print('\n')
print(b)
