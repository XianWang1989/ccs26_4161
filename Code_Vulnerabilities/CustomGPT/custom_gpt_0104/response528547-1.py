
# -*- coding: utf-8 -*-
import sys

# Take input from command line
a = sys.argv[1]

# Convert the input string to bytes
b = eval(a)  # safely evaluate the string and convert it to a byte object

print(a)  # Print the original string
print('\n')
print(b)  # Print the byte representation
