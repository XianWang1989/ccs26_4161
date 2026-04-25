
x = 0
bool_value = False  # Avoid using 'bool' as it shadows the built-in type

def functionA(x):
    if x == 0:
        return True  # Return the new boolean value
    return False

def functionB(bool_value):
    print(bool_value)
    if bool_value:
        print("Halleluhja")

# Update the boolean value based on functionA
bool_value = functionA(x)
functionB(bool_value)

print(x, bool_value)
