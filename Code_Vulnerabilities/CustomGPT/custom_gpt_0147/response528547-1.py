
# -*- coding: utf-8 -*-
import sys

# Capture the input from command line
a = sys.argv[1]

# Use eval to convert the input string representation to actual bytes
b = eval(a)

# Print the original string and the byte representation
print(a)
print('\n')
print(b)
