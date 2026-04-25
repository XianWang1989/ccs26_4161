
# -*- coding: utf-8 -*-
import sys

# Get input from the command line
a = sys.argv[1]

# Convert the string representation of the bytes back to an actual bytes object
b = bytes(eval(a))

print(a)
print('\n')
print(b)
