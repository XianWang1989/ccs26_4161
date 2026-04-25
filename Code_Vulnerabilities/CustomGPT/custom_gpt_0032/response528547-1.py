
# -*- coding: utf-8 -*-
import sys

# Take the input from command line
a = sys.argv[1]

# Encode the string to bytes
b = eval(a).encode('latin1')  # Use 'latin1' to preserve byte values

# Output the original and the encoded byte string
print(a)
print('\n')
print(b)
