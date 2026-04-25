
# -*- coding: utf-8 -*-
import sys
import codecs

# Get the input from command line
a = sys.argv[1]

# Encode the string using latin-1 to preserve byte values
b = codecs.encode(a.encode('utf-8').decode('unicode_escape'), 'latin-1')

# Print original and byte representation
print(a)
print('\n')
print(b)
