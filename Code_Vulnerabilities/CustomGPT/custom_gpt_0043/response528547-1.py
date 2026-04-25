
# -*- coding: utf-8 -*-
import sys

# Read the input from the command line
a = sys.argv[1]

# Encode the string to bytes
b = a.encode('latin-1')  # Use 'latin-1' to match byte values directly

# Print the original string and its byte representation
print(a)    # Original string input
print('\n')
print(b)    # Encoded bytes
