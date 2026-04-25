
# -*- coding: utf-8 -*-
import sys

# Take input from the command line
a = sys.argv[1]

# Convert the string representation of a byte literal to actual bytes
b = bytes(a, 'utf-8').decode('unicode_escape').encode('latin1')

# Print the original string and the byte representation
print(a)
print('\n')
print(b)
