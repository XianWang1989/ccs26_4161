
# -*- coding: utf-8 -*-
import sys

# Get the input from command line
a = sys.argv[1]

# Encode the string as bytes
b = a.encode('utf-8').decode('unicode_escape').encode('latin1')

# Print output
print(a)
print('\n')
print(b)
