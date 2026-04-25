
# -*- coding: utf-8 -*-
import sys
import codecs

# Get the input from command line
a = sys.argv[1]

# Encode the string to bytes
b = codecs.escape_encode(a.encode('utf-8'))[0]  # This maintains the byte representation

# Print the original and encoded byte-string
print(a)
print('\n')
print(b)
