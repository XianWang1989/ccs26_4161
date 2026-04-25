
# -*- coding: utf-8 -*-
import sys

# Take the input from the command line
a = sys.argv[1]

# Encode the string using 'utf-8' and print the original and byte representation
b = a.encode('utf-8').decode('unicode_escape').encode('latin1')

print(a)
print('\n')
print(repr(b))  # This will show the representation of bytes, similar to what you need.
