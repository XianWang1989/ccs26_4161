
# -*- coding: utf-8 -*-
import sys

# Accept input from command line
a = sys.argv[1]

# Convert to bytes
b = eval(a)  # Safely evaluate the input string

print(a)
print('\n')
print(b)
