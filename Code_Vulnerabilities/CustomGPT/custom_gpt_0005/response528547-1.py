
# -*- coding: utf-8 -*-
import sys

# Get the encrypted text from command line
a = sys.argv[1]

# Convert the string representation of bytes to actual bytes
b = eval(a.encode('utf-8').decode('unicode_escape'))

# Print the original string and the byte representation
print(a)
print('\n')
print(b)
