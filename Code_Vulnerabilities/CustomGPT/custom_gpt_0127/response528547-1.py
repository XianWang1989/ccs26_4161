
# -*- coding: utf-8 -*-
import sys

# Take input from command line
a = sys.argv[1]

# Convert the input string to bytes using the 'unicode_escape' encoding
b = bytes(a, 'utf-8').decode('unicode_escape').encode('latin1')

print(a)  # Original string
print('\n')
print(b)  # Byte representation
