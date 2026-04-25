
# -*- coding: utf-8 -*-
import sys

# Read the input from command line
input_str = sys.argv[1]

# Evaluate the string to convert the escape sequences to their byte representation
byte_output = eval(input_str)

print(input_str)  # Print the original string
print('\n')
print(byte_output)  # Print the byte representation
