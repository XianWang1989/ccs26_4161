
# -*- coding: utf-8 -*-
import sys

# Get input from command line
a = sys.argv[1]

# Encode the string to bytes
b = a.encode('utf-8')

# Print the original and the bytes representation
print(a)
print('\n')
print(b)  # This will display the byte representation
