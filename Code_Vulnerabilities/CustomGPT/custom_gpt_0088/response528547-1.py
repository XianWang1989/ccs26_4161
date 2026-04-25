
# -*- coding: utf-8 -*-
import sys

# Get input from command line
a = sys.argv[1]

# Interpret the string as a Python literal and encode it
b = eval(a)  # This safely evaluates the string to get the bytes representation

print(a)  # Original string
print('\n')
print(b)  # Output as bytes
