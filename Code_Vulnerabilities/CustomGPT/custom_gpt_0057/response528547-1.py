
# -*- coding: utf-8 -*-
import sys
import ast

a = sys.argv[1]
b = ast.literal_eval(a)  # Safely evaluate the string as a bytes literal

print(a)
print('\n')
print(b)
