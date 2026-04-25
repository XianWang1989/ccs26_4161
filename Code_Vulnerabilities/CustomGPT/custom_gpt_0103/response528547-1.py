
# -*- coding: utf-8 -*-
import sys

# Take the first command-line argument
a = sys.argv[1]

# Convert the input string to bytes
b = bytes(a, 'utf-8')

# Print the original input
print(a)
print('\n')

# Print the byte representation
print(b)
