
# -*- coding: utf-8 -*-
import sys
import ast

# Take input from the command line
a = sys.argv[1]

# Convert the input string into bytes
b = ast.literal_eval(a)

print(a)  # The original input string
print('\n')
print(b)  # The byte representation
