
# -*- coding: utf-8 -*-
import sys

# Get the input from the command line
a = sys.argv[1]
# Encode the string to bytes
b = a.encode('utf-8')

# To get the exact same representation as you intended, we can use the following:
b_represented = str(b)

# Print the original input and its byte representation
print(a)
print('\n')
print(b_represented)
