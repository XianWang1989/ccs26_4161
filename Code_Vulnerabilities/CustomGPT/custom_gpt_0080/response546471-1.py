
x = 0

def functionA(x):
    if x == 0:
        return True
    return False

def functionB(value):
    print(value)
    if value:
        print("Halleluhja")

# Get the boolean result from functionA
bool_value = functionA(x)
functionB(bool_value)

print(x, bool_value)
