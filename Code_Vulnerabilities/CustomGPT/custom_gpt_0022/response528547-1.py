
# -*- coding: utf-8 -*-
import sys
import ast

# Get the input from command line
a = sys.argv[1]

# Safely evaluate the input string to get the byte representation
b = ast.literal_eval(a)

print(a)  # Print the original input
print('\n')
print(b)  # Print the byte representation
