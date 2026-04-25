
# -*- coding: utf-8 -*-
import sys

def main():
    # Get the input string from command-line arguments
    a = sys.argv[1]

    # Encode the string to bytes while ensuring it maintains the escape
    # usable for decryption purposes.
    b = bytes(a, 'utf-8')

    print(a)
    print('\n')
    print(b)

if __name__ == "__main__":
    main()
