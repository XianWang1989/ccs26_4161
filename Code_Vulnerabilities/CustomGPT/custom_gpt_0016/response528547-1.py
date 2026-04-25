
# -*- coding: utf-8 -*-
import sys

# Get the input string from command line argument
a = sys.argv[1]

# Decode the string using 'unicode_escape' to interpret escape sequences
b = a.encode('utf-8').decode('unicode_escape').encode('utf-8')

# Print the original input and the byte string
print(a)
print('\n')
print(b)
