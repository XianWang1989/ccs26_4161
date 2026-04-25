
# -*- coding: utf-8 -*-
import sys

# Get the input from command line
input_string = sys.argv[1]

# Decode the input string representation of bytes
byte_string = eval(input_string)

# Print the original string and its byte representation
print(input_string)
print('\n')
print(byte_string)
