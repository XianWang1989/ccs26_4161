
# -*- coding: utf-8 -*-
import sys

# Read the input from the command line
a = sys.argv[1]

# Decode the input string to convert the escape sequences to their byte representation
b = eval(a)

# Print the original string and its byte representation
print(a)
print('\n')
print(b)
