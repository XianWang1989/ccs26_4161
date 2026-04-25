
# -*- coding: utf-8 -*-
import sys

# Take input from command line
a = sys.argv[1]

# Convert the string to bytes, handling the escape sequences
b = bytes(a, 'utf-8').decode('unicode_escape').encode('latin1')

print(a)  # Original input
print('\n')
print(b)  # Encoded bytes
