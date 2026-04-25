
# -*- coding: utf-8 -*-
import sys
import ast

# Take input from command line
a = sys.argv[1]

# Use ast.literal_eval to safely evaluate the string representation of bytes
# Instead of trying to manually replace backslashes
b = ast.literal_eval(a)  # This interprets the string in a way that converts escape sequences correctly.

print(a)
print('\n')
print(b)
