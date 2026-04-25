
x = 0
bool_value = False  # Avoid using 'bool' as it shadows the built-in type

def functionA(x):
    if x == 0:
        return True
    return False

def functionB(bool_value):
    print(bool_value)
    if bool_value is True:
        print("Hallelujah")

# Update bool_value based on the result from functionA
bool_value = functionA(x)
functionB(bool_value)

print(x, bool_value)
