
# -*- coding: utf-8 -*-
import sys

def main():
    # Get the command line argument
    input_string = sys.argv[1]

    # Convert the input into a bytes object using ASCII encoding
    # We need to evaluate the input string safely
    evaluated_bytes = eval(f"b'{input_string[2:]}'") if input_string.startswith("b'") else input_string.encode('utf-8')

    # Print the original and the bytes output
    print(input_string)  # Original input
    print('\n')
    print(evaluated_bytes)  # Encoded bytes

if __name__ == "__main__":
    main()
