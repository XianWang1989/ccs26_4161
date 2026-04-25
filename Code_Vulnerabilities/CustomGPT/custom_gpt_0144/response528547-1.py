# -*- coding: utf-8 -*-
import sys

# Get the input text from the command line argument
a = sys.argv[1]

# Print the original string
print(a)

# Convert the string to bytes using utf-8 encoding
b = a.encode('utf-8')

# Print the byte representation
print(b)
