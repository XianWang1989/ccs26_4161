
# -*- coding: utf-8 -*-
import sys

# Read input from command line
a = sys.argv[1]

# Encode the string while handling escape sequences
b = a.encode('utf-8').decode('unicode_escape').encode('latin1')

print(a)
print('\n')
print(b)
