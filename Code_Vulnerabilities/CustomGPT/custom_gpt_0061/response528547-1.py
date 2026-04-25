
# -*- coding: utf-8 -*-
import sys

# Read the input from command line
a = sys.argv[1]

# Convert the input string to a bytes object
# Correctly interpret the escaped sequences with eval
b = eval("bytes(" + repr(a) + ")")

print(a)
print('\n')
print(b)
