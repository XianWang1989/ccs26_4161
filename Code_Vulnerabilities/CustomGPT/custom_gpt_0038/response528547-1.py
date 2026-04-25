
# -*- coding: utf-8 -*-
import sys

def main():
    a = sys.argv[1]

    # Convert the input string to bytes using eval
    b = eval(f"b'{a[2:]}'")  # Removes the leading 'b' and encodes directly

    print(a)
    print('\n')
    print(b)

if __name__ == "__main__":
    main()
