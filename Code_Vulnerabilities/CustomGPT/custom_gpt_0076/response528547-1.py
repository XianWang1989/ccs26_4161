
# -*- coding: utf-8 -*-
import sys
import ast

# Get the input from command line
input_string = sys.argv[1]

# Convert input string to bytes
# Use ast.literal_eval to safely evaluate the input string
byte_string = ast.literal_eval(input_string)

print(input_string)
print('\n')
print(byte_string)
