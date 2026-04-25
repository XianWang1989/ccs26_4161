
# -*- coding: utf-8 -*-
import sys

# Get the input from command line
a = sys.argv[1]

# Encode the string to bytes and preserve the format
b = a.encode('utf-8').decode('unicode_escape').encode('latin1')

print(a)
print('\n')
print(b)
