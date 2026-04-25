
# -*- coding: utf-8 -*-
import sys

a = sys.argv[1]  # Get input from command line
b = a.encode('utf-8')  # Encode to bytes

# Print the original string and its byte representation
print(a)  # Print original input
print('\n')  
print(b)  # Print encoded bytes
