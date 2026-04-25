
# -*- coding: utf-8 -*-
import sys

# Get the input from command line
a = sys.argv[1]

# Encode the input string
b = a.encode('utf-8')

# Print the original string and the encoded bytes
print(a)
print('\n')
print(b)
