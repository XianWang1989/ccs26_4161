
import sys
import ast

a = sys.argv[1]
b = ast.literal_eval(a)

print(a)
print('\n')
print(b)
