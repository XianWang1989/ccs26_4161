
# -*- coding: utf-8 -*-
import sys

a = sys.argv[1]
# Decode the input string properly and then encode it to bytes
b = eval(a)  # Use eval to interpret the string as a bytes literal

print(a)
print('\n')
print(b)
