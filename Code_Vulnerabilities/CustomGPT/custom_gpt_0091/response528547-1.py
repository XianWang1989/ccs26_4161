
# -*- coding: utf-8 -*-
import sys

# Get the input from command line
a = sys.argv[1]

# Convert the input string to bytes
b = a.encode('utf-8')

# Print the original string
print(a)
print('\n')

# Print the bytes representation
print(b)
