
# -*- coding: utf-8 -*-
import sys

# Get input from command line
input_string = sys.argv[1]

# Decode the input string to bytes
# Use 'unicode_escape' to handle the escape sequences correctly
byte_output = bytes(input_string, 'utf-8').decode('unicode_escape').encode('latin1')

# Print the results
print(input_string)
print('\n')
print(byte_output)
