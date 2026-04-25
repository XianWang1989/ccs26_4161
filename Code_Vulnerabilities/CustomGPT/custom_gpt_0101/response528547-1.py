
# -*- coding: utf-8 -*-
import sys
import ast

a = sys.argv[1]
b = ast.literal_eval(a)  # Evaluates the string representation of bytes
print(a)
print('\n')
print(b)
