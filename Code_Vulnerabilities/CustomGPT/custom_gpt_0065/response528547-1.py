
# -*- coding: utf-8 -*-
import sys

# Get input from command line
a = sys.argv[1]

# Encode to bytes
b = a.encode('utf-8')

# Print original input and encoded bytes
print(a)
print('\n')
print(b)
