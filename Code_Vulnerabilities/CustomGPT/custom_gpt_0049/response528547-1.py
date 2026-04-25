
# -*- coding: utf-8 -*-
import sys
import ast

a = sys.argv[1]
# Convert the input string to bytes
b = bytes(ast.literal_eval(a))

print(a)
print('\n')
print(b)
