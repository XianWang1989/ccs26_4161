
import sys

a = sys.argv[1]
# Convert the string literal to bytes
b = bytes(a, 'utf-8').decode('unicode_escape').encode('latin1')

print(a)
print('\n')
print(b)
