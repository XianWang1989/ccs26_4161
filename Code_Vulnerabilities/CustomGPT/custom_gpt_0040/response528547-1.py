
# -*- coding: utf-8 -*-
import sys
import ast

# Get input from command line
a = sys.argv[1]

# Evaluate the string to convert it into actual bytes
b = ast.literal_eval(a)

print(a)
print('\n')
print(b)
