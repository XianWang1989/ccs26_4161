
# -*- coding: utf-8 -*-
import sys

# Get the input from command line
a = sys.argv[1]

# Decode the input string to a bytes object
b = eval(a)  # This evaluates the string as a Python expression

# Print the original string and the bytes
print(a)
print('\n')
print(b)
