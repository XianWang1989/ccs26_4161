
# -*- coding: utf-8 -*-
import sys

# Get input from command line
a = sys.argv[1]

# Convert the input string representation of bytes into actual bytes
b = eval(a)  # Using eval to interpret the input as bytes

# Print the results
print(a)
print('\n')
print(b)
