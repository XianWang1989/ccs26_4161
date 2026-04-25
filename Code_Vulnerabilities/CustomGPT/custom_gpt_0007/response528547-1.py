
# -*- coding: utf-8 -*-
import sys
import ast

# Take input from command line
a = sys.argv[1]

# Convert the string representation of a byte literal back to bytes
b = ast.literal_eval(a)

print(a)
print('\n')
print(b)
