
# -*- coding: utf-8 -*-
import sys

# Get input from command line
a = sys.argv[1]

# Convert to bytes
b = a.encode('utf-8')

print(a)  # Original string
print('\n')
print(b)  # Bytes representation
