
# -*- coding: utf-8 -*-
import sys

# Get input from command line
a = sys.argv[1]

# Decode the byte string and encode it back into bytes
b = eval(a).encode('utf-8')

print(a)
print('\n')
print(b)
