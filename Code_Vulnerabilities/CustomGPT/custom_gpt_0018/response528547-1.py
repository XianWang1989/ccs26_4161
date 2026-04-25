
# -*- coding: utf-8 -*-
import sys

# Take the original input
a = sys.argv[1]

# Convert the string representation of bytes to an actual bytes object
b = bytes(a, "utf-8").decode("unicode_escape").encode("latin1")

# Print the original input
print(a)
print('\n')

# Print the bytes representation
print(b)
