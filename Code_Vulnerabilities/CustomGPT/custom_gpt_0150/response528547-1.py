
# -*- coding: utf-8 -*-
import sys

# Get input from command line
a = sys.argv[1]

# Convert string to bytes, preserving the representation
b = a.encode('utf-8').decode('unicode_escape').encode('latin1')

print(a)
print('\n')
print(b)
