
# -*- coding: utf-8 -*-
import sys

# Retrieve input from command line
a = sys.argv[1]

# Evaluate the input string to interpret escape sequences
b = eval(a)

print(a)  # Original input
print('\n')
print(b)  # Byte representation
