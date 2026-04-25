
# -*- coding: utf-8 -*-
import sys
import ast

a = sys.argv[1]

# Convert the input string to bytes by evaluating it
b = ast.literal_eval(a)

print(a)
print('\n')
print(b)
