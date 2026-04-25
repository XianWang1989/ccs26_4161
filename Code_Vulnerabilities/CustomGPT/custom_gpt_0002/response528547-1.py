
# -*- coding: utf-8 -*-
import sys

# Take input from the command line
a = sys.argv[1]

# Encode the input string to bytes
b = a.encode('utf-8')

# Print the original string
print(a)
print('\n')

# Print the byte representation
print(b)
