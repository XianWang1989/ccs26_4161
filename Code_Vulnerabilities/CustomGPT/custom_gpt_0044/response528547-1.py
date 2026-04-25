
# -*- coding: utf-8 -*-
import sys

# Get the input from command line
a = sys.argv[1]

# Decode the string using 'unicode_escape' to interpret escape sequences
b = bytes(a, 'utf-8').decode('unicode_escape').encode('utf-8')

# Print the original input
print(a)
print('\n')

# Print the resulting bytes representation
print(b)
