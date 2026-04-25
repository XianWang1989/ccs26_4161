
# -*- coding: utf-8 -*-
import sys

# Fetch the argument from command line input
a = sys.argv[1]

# Convert the input string to bytes, interpreting escape sequences
b = bytes(a, 'utf-8').decode('unicode_escape').encode('latin1')

# Print the original string and the byte string
print(a)
print('\n')
print(b)
