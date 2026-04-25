
# -*- coding: utf-8 -*-
import sys

# Read the input from command line
a = sys.argv[1]

# Decode the input string as if it's a raw bytes representation
# First, strip the outer 'b' if present and evaluate the string
# Use the built-in evaluation function on the interpreted string
# This assumes that the input string is always well-formed and safe to evaluate
b = eval(a)

# Print the original string and the byte representation
print(a)
print('\n')
print(b)
