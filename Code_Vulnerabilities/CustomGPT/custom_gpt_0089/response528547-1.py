
# -*- coding: utf-8 -*-
import sys

# Read input from command line
a = sys.argv[1]

# Convert the escaped string to a bytes object
b = eval(f"b{a}")

# Print the original string and the bytes
print(a)
print('\n')
print(b)
