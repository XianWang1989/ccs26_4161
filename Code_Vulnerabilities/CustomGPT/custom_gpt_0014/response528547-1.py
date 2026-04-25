
# -*- coding: utf-8 -*-
import sys
import ast

# Get input from command line
a = sys.argv[1]

# Safely evaluate the string to get the bytes representation
b = ast.literal_eval(a)

print(a)  # Original input
print('\n')
print(b)  # Bytes representation
