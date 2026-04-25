
# -*- coding: utf-8 -*-
import sys

a = sys.argv[1]

# Use 'unicode_escape' to interpret the escape sequences correctly
b = bytes(a, 'utf-8').decode('unicode_escape').encode('latin1')

print(a)
print('\n')
print(b)
