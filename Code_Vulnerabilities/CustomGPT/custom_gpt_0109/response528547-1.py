
# -*- coding: utf-8 -*-
import sys

# Take input from command line
a = sys.argv[1]

# Encode to bytes without modifying the original representation
b = eval(a)  # Safely evaluate the string as a bytes literal

# Print original input and its byte representation
print(a)
print('\n')
print(b)
