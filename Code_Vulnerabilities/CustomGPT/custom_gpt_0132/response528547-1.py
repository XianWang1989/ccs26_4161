
# -*- coding: utf-8 -*-
import sys

# Get input from command line
a = sys.argv[1]

# Convert the input to bytes using the 'unicode_escape' encoding
b = a.encode('utf-8').decode('unicode_escape').encode('latin1')

# Print the original string and its bytes representation
print(a)
print('\n')
print(b)
