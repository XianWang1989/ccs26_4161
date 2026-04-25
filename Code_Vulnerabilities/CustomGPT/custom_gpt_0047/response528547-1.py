
# -*- coding: utf-8 -*-
import sys

# Get the input argument
a = sys.argv[1]

# Decode the string literal to bytes
b = eval(a)  # Safely evaluate the string literal

# Print the original string and the byte representation
print(a)
print('\n')
print(b)
