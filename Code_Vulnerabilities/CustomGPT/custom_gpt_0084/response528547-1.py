
# -*- coding: utf-8 -*-
import sys

# Get the input from the command line
a = sys.argv[1]

# Encode the string using unicode_escape to get the bytes
b = bytes(a, 'utf-8').decode('unicode_escape').encode('latin1')

print(a)
print('\n')
print(b)
