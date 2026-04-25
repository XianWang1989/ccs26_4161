
# -*- coding: utf-8 -*-
import sys

# Ensure that your input is a properly formatted byte string literal
a = sys.argv[1]

# If the input is in the form of a string representation of bytes (like 'b\x90\x89...'),
# you can use eval to convert it into actual bytes:
b = eval(a)

print(a)
print('\n')
print(b)  # This will output the byte representation
