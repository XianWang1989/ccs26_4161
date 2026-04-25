
# -*- coding: utf-8 -*-
import sys
import ast

if len(sys.argv) != 2:
    print("Usage: python3 test.py '<encrypted_string>'")
    sys.exit(1)

a = sys.argv[1]

# Convert the string input into bytes
b = ast.literal_eval(a)

print(a)
print('\n')
print(b)
