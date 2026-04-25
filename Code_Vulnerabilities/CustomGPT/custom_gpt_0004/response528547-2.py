
# -*- coding: utf-8 -*-
import sys
import ast

# Get input from command line
a = sys.argv[1]

# Safely evaluate the input string to bytes
try:
    b = ast.literal_eval(a)  # Converts the string representation to bytes
except Exception as e:
    print("Error parsing string:", e)
    sys.exit(1)

# Print the original and the bytes representation
print(a)
print('\n')
print(b)  # Outputs the actual byte sequence
