
# -*- coding: utf-8 -*-
import sys
import ast

# Get input from command line
a = sys.argv[1]

# Evaluate the input string to get the bytes representation
# This interprets the escape sequences correctly
b = bytes(ast.literal_eval(a))

print(a)
print('\n')
print(b)
