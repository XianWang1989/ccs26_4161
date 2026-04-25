
# -*- coding: utf-8 -*-
import sys

# Take the input from the command line
a = sys.argv[1]

# Convert the input string to bytes
b = a.encode('utf-8')

# Output the original string and its byte representation
print(a)
print('\n')
print(b)
