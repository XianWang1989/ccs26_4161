
# -*- coding: utf-8 -*-
import sys
import ast

# Get input from command line
input_string = sys.argv[1]

# Convert the input string to bytes
# Using ast.literal_eval to safely evaluate the string representation
bytes_output = bytes(ast.literal_eval(input_string))

print(input_string)
print('\n')
print(bytes_output)
