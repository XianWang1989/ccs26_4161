
# -*- coding: utf-8 -*-
import sys

# Get the input from command line
a = sys.argv[1]

# Use eval to interpret the string as bytes
b = eval(a)

print(a)
print('\n')
print(b)
