
# -*- coding: utf-8 -*-
import sys

# Get the command-line argument
a = sys.argv[1]

# Encode the string to bytes
# We can simply use 'unicode_escape' to handle the escape sequences
b = bytes(a, 'utf-8').decode('unicode_escape').encode('utf-8')

# Print the original string and the encoded bytes
print(a)
print('\n')
print(b)
