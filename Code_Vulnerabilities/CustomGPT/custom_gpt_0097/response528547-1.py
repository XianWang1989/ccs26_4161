
# -*- coding: utf-8 -*-
import sys

a = sys.argv[1]
# Convert the input to bytes using the 'unicode_escape' encoding
b = bytes(a, 'utf-8').decode('unicode_escape').encode('latin1')

print(a)
print('\n')
print(b)
