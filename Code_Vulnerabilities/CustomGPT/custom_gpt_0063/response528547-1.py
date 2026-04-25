
# -*- coding: utf-8 -*-
import sys
import ast

if len(sys.argv) < 2:
    print("Please provide the encrypted text as an argument.")
    sys.exit(1)

# Take input from command line
a = sys.argv[1]

try:
    # Convert the string representation of bytes to actual bytes
    b = ast.literal_eval(a)
except (ValueError, SyntaxError) as e:
    print("Error while converting to bytes:", e)
    sys.exit(1)

print(a)  # Original input
print('\n')
print(b)  # Bytes representation
