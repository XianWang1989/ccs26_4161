
# -*- coding: utf-8 -*-
import sys

if __name__ == "__main__":
    a = sys.argv[1]
    # Convert the input string to bytes using the 'unicode_escape' encoding
    b = bytes(a, 'utf-8').decode('unicode_escape').encode('latin1')

    print(a)
    print('\n')
    print(b)
