
# -*- coding: utf-8 -*-
import sys

# Get the input from command line
a = sys.argv[1]

# Evaluate the string to convert escape sequences into actual bytes
b = eval(a)

# Print the original string
print(a)
print('\n')

# Print the byte representation
print(b)
