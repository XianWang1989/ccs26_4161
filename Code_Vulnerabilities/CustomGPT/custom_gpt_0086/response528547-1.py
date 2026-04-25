
# -*- coding: utf-8 -*-
import sys
import ast

# Read input from command line
a = sys.argv[1]

# Safely evaluate the input string to get the byte representation
try:
    b = ast.literal_eval(a)
except (ValueError, SyntaxError) as e:
    print(f"Error evaluating input: {e}")
    sys.exit(1)

# Print results
print(a)
print('\n')
print(b)
