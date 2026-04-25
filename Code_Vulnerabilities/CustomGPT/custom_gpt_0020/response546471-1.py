
x = 0
bool_value = False  # Avoid using `bool` as a variable name since it's a built-in type

def functionA(x):
    if x == 0:
        return True
    return False  # Return False if the condition is not met

def functionB(bool_value):
    print(bool_value)
    if bool_value:
        print("Halleluhja")

# Capture the return value from functionA
bool_value = functionA(x)
functionB(bool_value)

print(x, bool_value)
