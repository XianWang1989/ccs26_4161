
# -*- coding: utf-8 -*-
import sys

a = sys.argv[1]
b = a.encode('utf-8')

# Converting bytes to a representation that matches input
byte_representation = repr(b)

print(a)
print('\n')
print(byte_representation)
