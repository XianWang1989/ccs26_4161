
x = 0

def functionA(x):
    if x == 0:
        return True
    return False

def functionB(bool_value):
    print(bool_value)  # Use parentheses for Python 3 compatibility
    if bool_value:
        print("Halleluhja")

# Call functionA and capture the returned boolean
bool_value = functionA(x)
functionB(bool_value)

print(x, bool_value)
