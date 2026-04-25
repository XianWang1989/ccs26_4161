
# -*- coding: utf-8 -*-
import sys

# Get the input from command line
a = sys.argv[1]

# Convert the string to bytes using eval to interpret the escape sequences
b = eval(a)

print(a)  # Original input string
print('\n')
print(b)  # Proper bytes representation
