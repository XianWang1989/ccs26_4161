
# -*- coding: utf-8 -*-
import sys

# Get input from command line
a = sys.argv[1]

# Encode the string into bytes
b = eval(a)  # Safely evaluate the input string as a bytes literal

print(a)  # Print the original string
print('\n')
print(b)  # Print the bytes
