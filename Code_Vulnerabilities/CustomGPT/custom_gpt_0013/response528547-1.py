
# -*- coding: utf-8 -*-
import sys

# Get input from the command line
a = sys.argv[1]

# Encode string to bytes by evaluating the string correctly
b = eval(a)

# Display the original input and the byte representation
print(a)
print('\n')
print(b)
