
# -*- coding: utf-8 -*-
import sys

# Take the input from the command line
a = sys.argv[1]

# Convert the string input into bytes by interpreting escape characters
b = bytes(a, 'utf-8').decode('unicode_escape').encode('latin1')

# Print the original string and its bytes representation
print(a)
print('\n')
print(b)
