
# -*- coding: utf-8 -*-
import sys

# Get the input from command line
a = sys.argv[1]

# Convert the string to bytes using unicode_escape
b = bytes(a, 'utf-8').decode('unicode_escape').encode('latin1')

# Print the original input
print(a)
print('\n')

# Print the bytes representation
print(b)
