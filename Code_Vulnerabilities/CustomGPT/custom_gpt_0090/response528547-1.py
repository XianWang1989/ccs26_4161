
# -*- coding: utf-8 -*-
import sys
import ast

a = sys.argv[1]
# Safely evaluate the string
b = ast.literal_eval(a)

print(a)
print('\n')
print(b)
