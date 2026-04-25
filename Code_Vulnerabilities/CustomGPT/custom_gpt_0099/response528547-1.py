
# -*- coding: utf-8 -*-
import sys

# Function to convert the input string representation of bytes to actual bytes
def decode_byte_string(byte_string):
    # Strip the leading 'b' and quotes, and then convert hex to bytes
    return bytes(eval(byte_string))

# Get the input from the command line
a = sys.argv[1]

# Decode the byte string from the input
b = decode_byte_string(a)

print(a)  # Original string
print('\n')
print(b)  # Byte representation
