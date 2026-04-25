
# -*- coding: utf-8 -*-
import sys
import ast

a = sys.argv[1]

# Evaluate the string to convert it into bytes
b = ast.literal_eval(a)

print(a)
print('\n')
print(b)
