
# -*- coding: utf-8 -*-
import sys

# Get the input string from command line arguments
a = sys.argv[1]

# Create a bytes object from the input string
b = bytes(a, 'utf-8')

# Print original string and its byte representation
print(a)
print('\n')
print(b)
