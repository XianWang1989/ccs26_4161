
# -*- coding: utf-8 -*-
import sys

a = sys.argv[1]
b = a.encode('utf-8')  # encoding the input string to bytes
print(a)
print('\n')
print(repr(b))  # using repr to show the byte sequence as a string
