
# -*- coding: utf-8 -*-
import sys

if len(sys.argv) > 1:
    a = sys.argv[1]

    # Convert the input string to print the bytes representation correctly
    b = bytes(a, 'utf-8').decode('unicode_escape').encode('latin1')

    print(a)
    print('\n')
    print(b)
else:
    print("Usage: python3 script.py '<encrypted_text>'")
